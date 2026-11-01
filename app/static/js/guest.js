(function () {
    var roomId = document.body.dataset.room;
    var selectedCategory = '';

    var buttons = document.querySelectorAll('.cat-btn');
    var errorBox = document.getElementById('error-msg');
    var submitBtn = document.getElementById('submit-btn');

    function showError(msg) { errorBox.textContent = msg; errorBox.style.display = 'block'; }
    function hideError() { errorBox.style.display = 'none'; }

    function setSending(sending) {
        submitBtn.disabled = sending;
        submitBtn.textContent = sending ? 'Sending...' : 'Send Request to Our Team';
    }

    buttons.forEach(function (btn) {
        btn.addEventListener('click', function () {
            buttons.forEach(function (b) { b.classList.remove('active'); });
            btn.classList.add('active');
            selectedCategory = btn.dataset.category;
            hideError();
        });
    });

    submitBtn.addEventListener('click', async function () {
        var guestName = document.getElementById('guest-name').value.trim();
        var description = document.getElementById('description').value.trim();

        if (!selectedCategory) { showError('Please select a category above.'); return; }
        if (description.length < 5) { showError('Please describe your issue in a little more detail.'); return; }

        setSending(true);
        hideError();

        try {
            var response = await fetch('/guest/' + roomId + '/submit', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    guest_name: guestName,
                    category: selectedCategory,
                    description: description
                })
            });
            var data = await response.json();

            if (data.success) {
                document.getElementById('main-form').style.display = 'none';
                document.getElementById('success-screen').style.display = 'block';
                document.getElementById('req-id-display').textContent = 'Request #' + data.request_id;
            } else {
                showError(data.error || 'Something went wrong. Please try again.');
                setSending(false);
            }
        } catch (err) {
            showError('Connection error. Please check your internet and try again.');
            setSending(false);
        }
    });

    document.getElementById('new-request-btn').addEventListener('click', function () {
        selectedCategory = '';
        document.getElementById('guest-name').value = '';
        document.getElementById('description').value = '';
        buttons.forEach(function (b) { b.classList.remove('active'); });
        setSending(false);
        document.getElementById('main-form').style.display = 'block';
        document.getElementById('success-screen').style.display = 'none';
        hideError();
    });
})();