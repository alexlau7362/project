<!-- templates/partials/_navbar.html -->
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="{% url 'home' %}">Shine Education</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <ul class="navbar-nav mr-auto">
            <li {% if '/' == request.path %} class="nav-item active mr-3"{% else %} class="nav-item mr-3" {% endif %}>
                <a class="nav-link" href="{% url 'home' %}">Home</a>
            </li>
            <li {% if 'about' in request.path %} class="nav-item active mr-3"{% else %} class="nav-item mr-3" {% endif %}>
                <a class="nav-link" href="{% url 'courses:about' %}">About</a>
            </li>
            <li {% if 'courses' in request.path %} class="nav-item active mr-3"{% else %} class="nav-item mr-3" {% endif %}>
                <a class="nav-link" href="{% url 'courses:courses' %}">Featured Courses</a>
            </li>
        </ul>
        <ul class="navbar-nav">
            {% if user.is_authenticated %}
                <li class="nav-item mr-3">
                    <span class="nav-link">Welcome, {{ user.username }}</span>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'accounts:logout' %}">Logout</a>
                </li>
            {% else %}
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'accounts:login' %}">Login</a>
                </li>
<!--                <li class="nav-item">
                    <a class="nav-link" href="{% url 'accounts:register' %}">Register</a>
                </li>    -->
            {% endif %}
        </ul>
    </div>
</nav>

