<!-- templates/tutors/noticeboard.html -->
{% extends 'base.html' %}
{% load static %}
{% block content %}
<div class="container">
    <h2 class="text-center">Noticeboard for {{ tutor.name }}</h2>
    {% if messages %}
    <div class="alert-container">
        {% for message in messages %}
        <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
            {{ message }}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
        {% endfor %}
    </div>
    {% endif %}
    {% if courses %}
    <div class="row">
        {% for course in courses %}
        <div class="col-md-6 col-lg-4 mb-4">
            <div class="card">
                {% if course.photo_main %}
                <img class="card-img-top" src="{{ course.photo_main.url }}" alt="{{ course.course_name }}">
                {% else %}
                <img class="card-img-top" src="{% static 'img/default_course.jpg' %}" alt="Default Course">
                {% endif %}
                <div class="card-body">
                    <h5 class="card-title">{{ course.course_name }}</h5>
                    <p class="card-text">Code: {{ course.course_code }}</p>
                    <p class="card-text">Location: {{ course.location }}</p>
                    <p class="card-text">Fee: ${{ course.fee }}</p>
                    <a href="{% url 'tutors:enquiry' course.id %}" class="btn btn-primary">Make Enquiry</a>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
    {% else %}
    <p>No courses assigned to you.</p>
    {% endif %}
</div>
{% endblock %}