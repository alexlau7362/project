{% extends 'base.html' %} {% block content %}
<section id="login" class="bg-light py-5">
    <div class="container">
      <div class="row">
        <div class="col-md-6 mx-auto">
          <div class="card">
            <div class="card-header bg-primary text-white">
              <h4><i class="fas fa-sign-in-alt"></i> Login</h4>
            </div>
            <div class="card-body">
             {% include 'partials/_alert.html' %}
              <form action="{% url 'accounts:login'  %}" method="POST">
                {% csrf_token %}
                <div class="form-group">
                  <label for="username">Username</label>
                  <input type="text" name="username"  class="form-control"/>
                </div>
                <div class="form-group">
                  <label for="password">Password</label>
                  <input
                    type="password"
                    name="password"
                    class="form-control"
                  />
                </div>

                <input
                  type="submit"
                  value="Login"
                  class="btn btn-secondary btn-block"
                />
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
{% endblock%} 

{% comment %} {% extends 'base.html' %}
{% load static %}

{% block content %}
<section class="section">
    <div class="container">
        <h1 class="course_name">Login</h1>
        
        <div class="columns">
            <div class="column is-half is-offset-one-quarter">
                <div class="card">
                    <div class="card-content">
                        <form method="post" action="{% url 'login' %}">
                            {% csrf_token %}
                            <div class="field">
                                <label class="label">Username</label>
                                <div class="control">
                                    <input class="input" type="text" name="username" required>
                                </div>
                            </div>
                            <div class="field">
                                <label class="label">Password</label>
                                <div class="control">
                                    <input class="input" type="password" name="password" required>
                                </div>
                            </div>
                            <div class="field">
                                <div class="control">
                                    <button class="button is-primary" type="submit">Login</button>
                                </div>
                            </div>
                        </form>
                        
                        <div class="has-text-centered mt-4">
                            <p>Don't have an account? <a href="{% url 'register' %}">Register here</a></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
{% endblock %}  {% endcomment %}