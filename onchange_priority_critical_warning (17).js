function onChange(control, oldValue, newValue, isLoading) {
    if (isLoading || newValue == '') {
        return;
    }

    if (newValue == '1') {
        g_form.showFieldMsg('priority', 'Priority is Critical. Verify Impact, Urgency and Assignment Group.', 'warning');
    }
}
