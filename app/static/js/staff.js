(function () {
    var openList = document.getElementById('open-list');
    var doneList = document.getElementById('done-list');
    var liveEl = document.getElementById('live');

    function el(tag, cls, text) {
        var e = document.createElement(tag);
        if (cls) e.className = cls;
        if (text !== undefined) e.textContent = text;
        return e;
    }

    function ago(iso) {
        if (!iso) return '';
        var mins = Math.max(0, Math.round((Date.now() - new Date(iso).getTime()) / 60000));
        if (mins < 1) return 'just now';
        if (mins < 60) return mins + ' min ago';
        return Math.floor(mins / 60) + ' h ' + (mins % 60) + ' min ago';
    }

    function header(r, badgeText, badgeClass) {
        var row = el('div', 'row');
        var left = el('div');
        left.appendChild(el('span', 'room', 'Room ' + r.room_number));
        left.appendChild(el('span', 'cat', r.category));
        row.appendChild(left);
        row.appendChild(el('span', 'badge ' + badgeClass, badgeText));
        return row;
    }

    function openCard(r) {
        var card = el('div', 'card ' + r.priority);
        card.appendChild(header(r, r.status.replace('_', ' '), r.status));
        card.appendChild(el('div', 'desc', r.description));
        card.appendChild(el('div', 'meta',
            r.guest_name + ' · ' + ago(r.submitted_at) + ' · ' + r.priority + ' priority'));

        var actions = el('div', 'actions');
        if (r.status !== 'in_progress') {
            var start = el('button', 'btn-start', 'Start');
            start.addEventListener('click', function () { act(r.id, 'in_progress'); });
            actions.appendChild(start);
        }
        var done = el('button', 'btn-done', 'Mark resolved');
        done.addEventListener('click', function () { act(r.id, 'resolved'); });
        actions.appendChild(done);
        card.appendChild(actions);
        return card;
    }

    function doneCard(r) {
        var card = el('div', 'card done');
        card.appendChild(header(r, 'resolved', ''));
        card.appendChild(el('div', 'meta', r.description));
        if (r.resolution_note) card.appendChild(el('div', 'meta', 'Note: ' + r.resolution_note));
        return card;
    }

    function fill(container, items, builder, emptyText) {
        container.replaceChildren();
        if (!items.length) {
            container.appendChild(el('div', 'empty', emptyText));
            return;
        }
        items.forEach(function (r) { container.appendChild(builder(r)); });
    }

    function load() {
        fetch('/staff/api/requests')
            .then(function (res) { return res.json(); })
            .then(function (data) {
                document.getElementById('open-count').textContent = data.open.length;
                fill(openList, data.open, openCard, 'No open requests. All quiet.');
                fill(doneList, data.resolved, doneCard, 'Nothing resolved yet.');
                document.title = (data.open.length ? '(' + data.open.length + ') ' : '') + 'Buffalo Staff';
            });
    }

    function act(id, status) {
        var note = '';
        if (status === 'resolved') note = prompt('Resolution note (optional):') || '';
        fetch('/staff/api/requests/' + id + '/status', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ status: status, note: note })
        })
            .then(function (res) { return res.json(); })
            .then(function (d) {
                if (!d.success) alert(d.error || 'Something went wrong');
                load();
            });
    }

    var socket = io();
    socket.on('connect', function () {
        socket.emit('join_staff');
        liveEl.textContent = 'Live';
        liveEl.className = 'live on';
    });
    socket.on('disconnect', function () {
        liveEl.textContent = 'Offline';
        liveEl.className = 'live';
    });
    socket.on('new_request', load);
    socket.on('request_updated', load);

    load();
    setInterval(load, 60000);
})();