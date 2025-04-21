<!-- templates/pages/index.html -->
{% extends 'base.html' %}
{% load static %}
{% load humanize %}
{% block content %}
<section id="services" class="py-5 bg-secondary text-white">
  <div class="container">
    <div class="row text-center">
      <div class="col-md-4">
        <hr />
        <h3>Excellent Services</h3>
        <p>Indoor and outdoor activities for children</p>
      </div>
      <div class="col-md-4">
        <hr />
        <h3>Qualified Tutors</h3>
        <p>Tutors qualification and excellent experiences</p>
      </div>
      <div class="col-md-4">
        <hr />
        <h3>Course Admission Criteria</h3>
        <p>Language, Communication, Childcare, Art, Music, Science, Math</p>
      </div>
    </div>
  </div>
</section>

<!-- Running photos -->
<div id="demo" class="carousel slide bg-info" data-ride="carousel">
  <ul class="carousel-indicators">
    <li data-target="#demo" data-slide-to="0" class="active"></li>
    <li data-target="#demo" data-slide-to="1"></li>
    <li data-target="#demo" data-slide-to="2"></li>
    <li data-target="#demo" data-slide-to="3"></li>
    <li data-target="#demo" data-slide-to="4"></li>
    <li data-target="#demo" data-slide-to="5"></li>
  </ul>
  <div class="carousel-inner bg-dark">
    <style>
      .carousel-item img {
        width: 80%;
        max-height: 650px;
        object-fit: cover;
        margin: auto;
        transition: transform 0.2s;
      }
    </style>
    <div class="carousel-item active mb-3">
      <img src="{% static 'img/gallery-1.png' %}" class="mx-auto d-block" alt="Kids">
    </div>
    <div class="carousel-item mb-3">
      <img src="{% static 'img/gallery-2.png' %}" class="mx-auto d-block" alt="Kids">
    </div>
    <div class="carousel-item mb-3">
      <img src="{% static 'img/gallery-3.png' %}" class="mx-auto d-block" alt="Kids">
    </div>
    <div class="carousel-item mb-3">
      <img src="{% static 'img/gallery-4.png' %}" class="mx-auto d-block" alt="Kids">
    </div>
    <div class="carousel-item mb-3">
      <img src="{% static 'img/gallery-5.png' %}" class="mx-auto d-block" alt="Kids">
    </div>
    <div class="carousel-item mb-3">
      <img src="{% static 'img/gallery-6.png' %}" class="mx-auto d-block" alt="Kids">
    </div>
  </div>
  <a class="carousel-control-prev" href="#demo" data-slide="prev">
    <span class="carousel-control-prev-icon"></span>
  </a>
  <a class="carousel-control-next" href="#demo" data-slide="next">
    <span class="carousel-control-next-icon"></span>
  </a>
</div>

<!-- Showcase -->
<section id="showcase">
  <div class="container text-center">
    <div class="home-search p-5">
      <div class="overlay p-5">
        <h1 class="display-4 mb-4">Searching Just Got So Easy</h1>
        <p class="lead">Must have a suitable course for your children</p>
        <div class="search">
          <form action="{% url 'courses:search' %}">
            <div class="form-row">
              <div class="col-md-4 mb-3">
                <label for="keywords" class="sr-only">Keywords</label>
                <input
                  id="keywords"
                  type="text"
                  name="keywords"
                  class="form-control"
                  placeholder="Keyword (start-date, end-date, etc)"
                />
              </div>
              <div class="col-md-4 mb-3">
                <label class="sr-only">Course_name</label>
                <input
                  type="text"
                  name="course_name"
                  class="form-control"
                  placeholder="Course_name"
                />
              </div>
              <div class="col-md-4 mb-3">
                <label class="sr-only">Location</label>
                <select name="location" class="form-control">
                  <option selected="true" value="">Location (All)</option>
                  {% for key,value in location_choices.items %}
                  <option value="{{ key }}">{{ value }}</option>
                  {% endfor %}
                </select>
              </div>
            </div>
            <div class="form-row">
              <div class="col-md-6 mb-3">
                <label class="sr-only">Start-date</label>
                <select name="start_date" class="form-control">
                  <option selected="true" value="">Start-date (Any)</option>
                  {% for key,value in start_date_choices.items %}
                  <option value="{{ key }}">{{ value }}</option>
                  {% endfor %}
                </select>
              </div>
              <div class="col-md-6 mb-3">
                <select name="fee" class="form-control" id="type">
                  <option selected="true" value="">Fee (Any)</option>
                  {% for key,value in fee_choices.items %}
                  <option value="{{ key }}">{{ value }}</option>
                  {% endfor %}
                </select>
              </div>
            </div>
            <button class="btn btn-secondary btn-block mt-4" type="submit">
              Submit
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Courses -->
<section id="courses" class="py-5">
  <div class="container">
      <h2 class="text-center">Featured Courses</h2>
      <div class="row">
          {% if courses %}
              {% for course in courses %}
                  <div class="col-md-6 col-lg-4 mb-4">
                      <div class="card listing-preview">
                          {% if course.photo_main %}
                              <img class="card-img-top" src="{{ course.photo_main.url }}" alt="">
                          {% else %}
                              <img class="card-img-top" src="{% static 'img/default_course.jpg' %}" alt="">
                          {% endif %}
                          <div class="card-img-overlay">
                              <h2>
                                  <span class="badge badge-secondary text-white">${{ course.fee }}</span>
                              </h2>
                          </div>
                          <div class="card-body">
                              <div class="listing-heading text-center">
                                  <h4 class="text-primary">{{ course.course_name }}</h4>
                                  <p>
                                      <i class="fas fa-map-marker text-secondary"></i> {{ course.location }}
                                  </p>
                              </div>
                              <hr>
                              <div class="row py-2 text-secondary">
                                  <div class="col-6">
                                      <i class="fas fa-th-large"></i> Course Code: {{ course.course_code }}
                                  </div>
                                  <div class="col-6">
                                      <i class="fas fa-user"></i> Tutor: {{ course.tutor.name }}
                                  </div>
                              </div>
                              <div class="row text-secondary pb-2">
                                  <div class="col-6">
                                      <i class="fas fa-clock"></i> Posted: {{ course.published_date|timesince }} Ago
                                  </div>
                              </div>
                              <hr>
                              <a href="{% url 'courses:course_detail' course.id %}" class="btn btn-primary btn-block">More Info</a>
                          </div>
                      </div>
                  </div>
              {% endfor %}
          {% else %}
              <div class="col-md-12">
                  <p>No Courses Available</p>
              </div>
          {% endif %}
      </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h1 class="course_name">Welcome to Our Course Platform</h1>
    <div class="columns is-multiline">
      {% for course in courses %}
      <div class="column is-one-third">
        <div class="card">
          {% if course.photo_1 %}
          <div class="card-image">
            <figure class="image is-4by3">
              <img src="{{ course.photo_1.url }}" alt="{{ course.course_name }}">
            </figure>
          </div>
          {% endif %}
          <div class="card-content">
            <h2 class="course_name is-4">{{ course.course_name }}</h2>
            <p class="subcourse_name is-6">Code: {{ course.course_code }}</p>
            <div class="content">
              <p><strong>Location:</strong> {{ course.location }}</p>
              <p><strong>Fee:</strong> ${{ course.fee }}</p>
              <p><strong>Class Size:</strong> {{ course.class_size }} students</p>
              <p><strong>Start Date:</strong> {{ course.start_date }}</p>
            </div>
            <a href="{% url 'course_detail' course.id %}" class="btn btn-primary">View Details</a>
          </div>
        </div>
      </div>
      {% empty %}
      <div class="column">
        <p>No courses available.</p>
      </div>
      {% endfor %}
    </div>
  </div>
</section>

<!-- Pages -->
<div class="container">
  <div class="row">
    {% for page in pages %}
    <div class="col" style="background-color:lavender;">
      {% if page.photo_main %}
      <img src="{{ page.photo_main.url }}" alt="{{ page.medium|default:'Page' }}" class="img-fluid" />
      {% else %}
      <img src="{% static 'img/default_page.jpg' %}" alt="Default Page" class="img-fluid" />
      {% endif %}
      <h4>{{ page.medium|default:"Untitled" }}</h4>
      <div class="lead">
        {{ page.admission_criteria|default:"No criteria provided" }}
        <a href="#" class="btn btn-success">Learn More</a>
      </div>
    </div>
    {% empty %}
    <div class="col" style="background-color:lavender;">
      <img src="{% static 'img/logo.png' %}" alt="Logo" class="img-fluid" />
      <h2>Under Construction</h2>
      <div class="lead">
        <a href="#" class="btn btn-success">Learn More</a>
      </div>
    </div>
    {% endfor %}
  </div>
</div>
{% endblock %}