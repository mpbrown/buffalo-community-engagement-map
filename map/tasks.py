from __future__ import absolute_import
from celery import shared_task
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import json

@shared_task
def send_email(formjson):
    data = json.loads(formjson)
    subject = 'Follow up from UB Spark Workshop on Community Engagement'
    template_name = 'email.html'
    
    # Build context
    context = {
        'organization_name': data['organization_name'],
        'why_interesting': data['why_interesting'],
        'services': data['services'],
        'contribute': data['contribute'],
        'staff_member_name': data['staff_member_name'],
        'staff_member_title': data['staff_member_title'],
        'staff_member_email': data['staff_member_email'],
        'student_name': data['student_name'],
        'student_email': data['student_email']
    }

    # Render HTML content to string
    html_content = render_to_string(template_name=template_name, context=context)

    # Build EmailMessage with stripped HTML tags
    msg = mail.message.EmailMultiAlternatives(subject=subject, body=strip_tags(html_content), to=[data['student_email']])

    # Attach alternative with HTML content
    msg.attach_alternative(html_content, "text/html")

    # Add msg to messages list
    msg.send()