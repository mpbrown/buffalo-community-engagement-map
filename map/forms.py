from django import forms

class EmailOrganizationForm(forms.Form):
    organization_name = forms.CharField(
        label="Organization you'd be most interested in working with",
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    why_interesting = forms.CharField(
        label="Write one sentence about why this organization is interesting. How does it/could it connect to your life?", 
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))

    services = forms.CharField(
        label="Review the programs and services offered by this organization. Which ones could you contribute to?",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))

    contribute = forms.CharField(
        label="Write one sentence about how you believe you can contribute to the organization.",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))

    staff_member_name = forms.CharField(
        label="Staff member name",
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    staff_member_name = forms.CharField(
        label="Staff member title",
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    staff_member_email = forms.EmailField(
        label="Staff member email",
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    student_email = forms.EmailField(
        label="Your UB email address",
        widget=forms.TextInput(attrs={'class': 'form-control'}))