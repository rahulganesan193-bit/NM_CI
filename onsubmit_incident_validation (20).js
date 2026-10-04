function onSubmit() {
    var shortDescription = g_form.getValue('short_description');

    if (shortDescription == '') {
        g_form.showErrorBox('short_description', 'Short description is mandatory before submitting the Incident.');
        return false;
    }

    if (g_form.getValue('impact') == '1' && g_form.getValue('assigned_to') == '') {
        g_form.showErrorBox('assigned_to', 'Assigned To is mandatory for High impact incidents.');
        return false;
    }

    return true;
}
