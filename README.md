# supreme-eureke

## SECTION A

### 1. Give examples of different integration protocols you have come across and give example scripts in python 3 on how to achieve each one. (10 pts)

#### 1. RESTful API

RESTful APIs are widely used for communication between systems. They are based on standard HTTP methods (GET, POST, PUT, PATCH and DELETE) and often use JSON for data exchange.

**Example:**

```python
import requests

# Define API endpoint
url = "https://api.example.com/users"

# Example GET request
response = requests.get(url)
print("GET Response:", response.json())

# Example POST request
new_user = {"username": "john_doe", "email": "john.doe@example.com"}
post_response = requests.post(url, json=new_user)
print("POST Response:", post_response.json())
```

#### 2. GraphQL

GraphQL is a query language for APIs that allows clients to request only the data they need. It provides a more flexible and efficient alternative to traditional REST APIs.

**Example:**

```python
import requests

# Define GraphQL endpoint
url = "https://api.example.com/graphql"

# Example GraphQL query
query = """
    query {
        user(id: 1) {
            id
            username
            email
        }
    }
"""

# Send GraphQL query
response = requests.post(url, json={"query": query})
print("GraphQL Response:", response.json())
```

### 2. Give a walkthrough of how you will manage a data streaming application sending one million notifications every hour while giving examples of technologies and configurations you will use to manage load and asynchronous services. (10 pts)

- Effectively managing a data streaming application that sends one million notifications every hour demands a strategic approach. In this walkthrough, I'll outline the key strategies and technologies I would employ to manage the load efficiently and ensure seamless asynchronous service processing.

### Technologies

#### 1. Apache Kafka for Data Streaming

- For robust data streaming, Apache Kafka is the chosen tool. Its selection is rooted in its unparalleled scalability, fault tolerance, and support for real-time event processing. Kafka's distributed architecture ensures high throughput and low latency, making it an ideal choice for handling the substantial load of one million notifications per hour.

#### 2. Redis for Caching

- Caching, a critical aspect of performance optimization, is entrusted to Redis. Redis stands out for its exceptional speed and versatility as an in-memory data store. Its ability to handle frequently accessed data efficiently aligns with the goal of improving data retrieval speed for our streaming application.

#### 3. Celery for Asynchronous Processing

- Asynchronous task handling is a key component of our strategy, and Celery is the chosen tool for this purpose. Celery's distributed architecture and support for various message brokers make it a robust solution for managing asynchronous tasks, ensuring optimal performance and reliability.

### Load Management Strategies

### 1. Horizontal Scaling

- To address the challenge of high load, horizontal scaling is implemented by deploying multiple instances of the application. Nginx is selected as the load balancer due to its versatility and ability to evenly distribute traffic among the instances.

### 2. Performance Monitoring

- Monitoring the system's performance is paramount for identifying bottlenecks and ensuring optimal operation. Prometheus and Grafana are chosen for their robust monitoring capabilities.

### 3. Give examples of different encryption/hashing methods you have come across (one way and two way) and give example scripts in python 3 on how to achieve each one. (20 pts)

#### One-Way Encryption/Hashing Methods

##### 1. SHA-256 Hashing

- SHA-256 is a widely used one-way hashing algorithm that produces a fixed-size output, regardless of the input size. It is commonly used to store password hashes securely.

**Example:**

```python
import hashlib

def hash_password(password):
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# Example usage
password = "myStrongPassword"
hashed_password = hash_password(password)
print("Hashed Password:", hashed_password)
```

##### 2. bcrypt for Password Hashing

- bcrypt is a key derivation function designed for secure password hashing. It incorporates a salt and a cost factor to increase computational complexity, making it resistant to brute-force attacks.

**Example:**

```python
import bcrypt

def hash_password(password):
    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password

# Example usage
password = "myStrongPassword"
hashed_password = hash_password(password)
print("Hashed Password:", hashed_password)
```

#### Two-Way Encryption Methods

##### 1. Fernet Symmetric Encryption

- Fernet is a symmetric encryption method using a shared secret key. It provides a simple and secure way to encrypt and decrypt data.

**Example:**

```python
from cryptography.fernet import Fernet

def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(data.encode())
    return cipher_text

def decrypt_data(cipher_text, key):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(cipher_text).decode()
    return decrypted_data

# Example usage
shared_key = Fernet.generate_key()
data_to_encrypt = "myStrongPassword"
encrypted_data = encrypt_data(data_to_encrypt, shared_key)
decrypted_data = decrypt_data(encrypted_data, shared_key)

print("Encrypted Data:", encrypted_data)
print("Decrypted Data:", decrypted_data)
```

##### 2. RSA Asymmetric Encryption

- RSA is an asymmetric encryption algorithm using public and private key pairs. It is commonly used for secure communication and digital signatures.

**Example:**

```python
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def encrypt_data(data, public_key):
    cipher_text = public_key.encrypt(
        data.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return cipher_text

def decrypt_data(cipher_text, private_key):
    decrypted_data = private_key.decrypt(
        cipher_text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    ).decode()
    return decrypted_data

# Example usage
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

data_to_encrypt = "myStrongPassword"
encrypted_data = encrypt_data(data_to_encrypt, public_key)
decrypted_data = decrypt_data(encrypted_data, private_key)

print("Encrypted Data:", encrypted_data)
print("Decrypted Data:", decrypted_data)
```

## SECTION B

### 1. Create a login and a success page in Django. A mockup of the created pages should also be submitted. The mockups should have been created by using advanced design/wireframe tools thus showcasing prowess in usage of the tools and use of production server deployments on uwsgi/nginx. Ensure that the sessions are well and securely managed.(60 pts)

#### Introduction

- This Django project aims to create a user management system with features for user registration, authentication, and profile management. The project follows a modular structure with distinct components for models, forms, views, and URLs.

## Running the project

- To run the project ensure you have the docker desktop and then run the command

```bash
$ docker-compose -f local.yml up
```

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Running migrations

```bash
$ docker compose -f local.yml run --rm django python manage.py migrate
$ docker compose -f local.yml run --rm django python manage.py createsuperuser
```

#### Design

- To view the design go to [InterIntel](https://www.figma.com/file/bj9G2Ki6wwj8kamlAUsRgM/InterIntel?type=design&node-id=3%3A5&mode=design&t=6XHRV4oiwIA3j1m6-1)

#### Login Page Design

![Login_page](https://github.com/qinyanjuidavid/supreme-eureke/assets/49823575/fea33034-6b96-493e-895a-944162339362)

#### Success Page Design

![success_page](https://github.com/qinyanjuidavid/supreme-eureke/assets/49823575/67df3665-f5f2-4373-9c6d-22e3d248680d)

#### Code Overview

##### models

- In Django, models are Python classes that define the structure of database tables and the relationships between them. They serve as a blueprint for creating, querying, updating, and deleting records in the database. Models encapsulate the application's data structure and business logic. In my code i have the

###### Tracking model

- The tracking model is an Abstract model which helps me to track when an object was created or updated, the purpose for this model is to prevent repetition of the updated_at and created_at field.

```python
class Constants(models.TextChoices):
    """
    A class to define constants YES and NO for flag fields.
    """

    YES = "Yes", ("Yes")
    NO = "No", ("No")


class TrackingModel(models.Model):
    """
    Abstract base model for tracking creation and update timestamps.
    """

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    updated_flag = models.CharField(
        _("updated flag"),
        max_length=3,
        choices=Constants.choices,
        default=Constants.NO,
    )

    class Meta:
        abstract = True
```

###### User model

- In the user model i have am extending the Abstract base user, the purpose for this model is to help in storing the data that is related to the user, such as name, email, phone, is_active, etc

```python
class RoleChoices(models.TextChoices):
    """
    Enumeration of possible user roles.
    """

    SUPERUSER = "SUPERUSER", ("SUPERUSER")


class User(AbstractBaseUser, PermissionsMixin, TrackingModel):
    """
    Custom User model representing a user of the application.
    """

    name = models.CharField(_("full name"), blank=True, max_length=255)
    email = models.EmailField(_("email address"), unique=True)
    phone_no = models.CharField(
        _("phone number"),
        max_length=56,
        blank=True,
        null=True,
    )
    is_staff = models.BooleanField(_("staff"), default=False)
    is_active = models.BooleanField(_("active"), default=False)
    is_superuser = models.BooleanField(_("superuser"), default=False)
    role = models.CharField(
        _("role"),
        max_length=20,
        choices=RoleChoices.choices,
        # default=RoleChoices.,
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        help_text=_("The groups this user belongs to."),
        related_name="user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name=_("user permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="user_set",
        related_query_name="user",
    )
    timestamp = models.DateTimeField(_("date joined"), auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name_plural = "users"
        ordering = ["-id"]

    def __str__(self):
        """
        Returns a string representation of the user object.

        Returns:
            str: The user's email address.
        """
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to the user.

        Args:
            subject (str): The subject of the email.
            message (str): The content of the email.
            from_email (str, optional): The sender's email address.
            Defaults to None.
            **kwargs: Additional keyword arguments accepted by Django's
            `send_mail` function.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def superuser(self):
        """
        Property indicating whether the user is a superuser.

        Returns:
            bool: True if the user is a superuser, False otherwise.
        """
        return self.is_superuser

    @property
    def staff(self):
        """
        Property indicating whether the user is a staff member.

        Returns:
            bool: True if the user is a staff member, False otherwise.
        """
        return self.is_staff

    @property
    def active(self):
        """
        Property indicating whether the user account is active.

        Returns:
            bool: True if the user account is active, False otherwise.
        """
        return self.is_active
```

###### Profile model

- The profile model is a model that helps in storing the other data that are releted to the user such as profile picture, gender, bio and date_of_birth. In my case i always prefer separating the users profile based on the various roles defined by the project.

```python
class Profile(models.Model):
    """
    User profile
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="%(class)s_profile",
    )

    profile_image = models.ImageField(
        _("profile picture"),
        upload_to="profile_images",
        null=True,
        blank=True,
        default="default.png",
    )
    bio = models.TextField(_("bio"), max_length=500, null=True, blank=True)
    gender = models.CharField(
        _("gender"),
        max_length=1,
        choices=GenderChoices.choices,
        default=GenderChoices.PREFER_NOT_TO_SAY,
    )
    date_of_birth = models.DateField(_("date of birth"), null=True, blank=True)

    def __str__(self):
        return self.user.email

    class Meta:
        abstract = True


class SuperUser(Profile):
    """
    Model representing app Superusers.
    """

    def __str__(self):
        return self.user.email or self.user.phone_no

    class Meta:
        verbose_name_plural = "Super Users"
        ordering = ["-id"]
```

##### Forms

- In Django, forms play a crucial role in handling user input, validation, and interaction with the application's data models. Forms provide a convenient way to create HTML forms and handle user-submitted data in a structured manner. Django forms are defined as Python classes and are part of the Django forms library.

###### UserSignupForm

- The UserSignupForm is responsible for handling user registration and signup. It collects information such as name, email, phone number, password, and password confirmation from the user.

```python
class UserSignupForm(forms.ModelForm):
    """
    A form for user registration/signup.
    """

    name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=156, required=True)
    phone = forms.CharField(max_length=20, required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_confirmation = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput,
    )

    class Meta:
        """
        Meta class for UserSignupForm.

        Specifies the model and fields to be used in the form.
        """

        model = User
        fields = ("name", "phone", "email", "password", "password_confirmation")

    def clean(self):
        """
        Clean method for additional form-wide validation.

        Raises:
            forms.ValidationError: If the passwords do not match.
        Returns:
            dict: The cleaned form data.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password and password_confirmation and password != password_confirmation:
            raise forms.ValidationError("The passwords do not match.")

        return cleaned_data

    @transaction.atomic
    def save(self, commit=True):
        """
        Save method to create and save a new user instance.

        Args:
            commit (bool): If True, save the user instance to the database.

        Returns:
            User: The created user instance.
        """
        user = super().save(commit=False)
        user.is_active = True
        user.role = RoleChoices.SUPERUSER
        user.phone_no = self.cleaned_data["phone"]
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

```

###### CustomAuthenticationForm

- The CustomAuthenticationForm extends Django's built-in AuthenticationForm, customizing the login form. It replaces the default username field with an email field.

```python
class CustomAuthenticationForm(AuthenticationForm):
    """
    A custom authentication form that extends Django's AuthenticationForm.
    """

    email = EmailField(
        label=_("Email address"),
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        fields = ["email", "password"]

    field_order = ["email", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "username" in self.fields:
            del self.fields["username"]
```

##### Views

- In Django, views are responsible for processing user requests, handling business logic, and returning appropriate responses, often in the form of HTML pages. Views determine what content is displayed to the user and how interactions with that content are managed.

###### SignupView

- The SignupView is a class-based view used for user registration and signup. It leverages Django's CreateView to simplify the creation of a view for creating a new object (in this case, a user).

```python
class SignupView(CreateView):
    """
    View for user registration/signup.
    """

    model = User
    form_class = UserSignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:login")

    def get_context_data(self, **kwargs):
        """
        Get the context data for rendering the template.
        """
        kwargs["user_type"] = RoleChoices.SUPERUSER
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        """
        Process a valid form submission.
        """
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))
```

###### LoginView

- The loginView function-based view is responsible for handling user login.

```python
def loginView(request):
    """
    View for user login.
    """
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login success.")
                # Redirect to the success page.
                return HttpResponseRedirect(reverse("accounts:home"))
    else:
        form = CustomAuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})

```

###### HomeView

- In my case the HomeView is the one responsible for showcasing the success page after the user logs in.

```python
@login_required
def HomeView(request):
    """
    View for the home page.
    """
    userQuery = User.objects.all()
    context = {
        "users": userQuery,
    }
    return render(request, "pages/home.html", context)

```

##### Templates

###### base.html

- The base.html serves as the foundational template for the entire application.
  It defines the overall structure of the HTML document, including meta tags, Bootstrap CSS links, and the necessary JavaScript scripts.
- The template includes a navigation bar block ({% block navBar %}) and a content block ({% block content %}) that can be overridden by other templates.

```html
<!DOCTYPE html>
{%load static%} {%load crispy_forms_tags%}
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <!-- Bootstrap CSS -->
    <link
      href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
      rel="stylesheet"
      integrity="sha384wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN"
      crossorigin="anonymous"
    />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
      crossorigin="anonymous"
    />

    <title>{%block head_title%}{%endblock%} | InterIntel!</title>
  </head>
  <body>
    {%block navBar%} {%endblock%}
    <!-- messages -->
    {% if messages %}
    <div class="container">
      <div class="messages p-3">
        {% for message in messages %} {% if message.tags %}
        <div
          class="alert {% if message.tags == 'error' %}alert-danger{% endif %} {% if message.tags == 'success' %}alert-success{% endif %} {% if message.tags == 'warning' %}alert-warning{% endif %} {% if message.tags == 'info' %}alert-info{% endif %}"
          role="alert"
        >
          {{ message }}
        </div>
        {% else %}
        <div class="alert alert-secondary" role="alert">{{ message }}</div>
        {% endif %} {% endfor %}
      </div>
    </div>
    {% endif %} {%block content%} {%endblock%}

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
      crossorigin="anonymous"
    ></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
    -->
  </body>
</html>
```

###### login.html

- The login.html template extends base.html and focuses specifically on the login functionality. It includes a form for user login, styled using Bootstrap and Crispy Forms.
- Users can input their email and password, with options for "Remember Me" and a link to reset the password. The template provides a clean and user-friendly interface for the login process.

```html
{% extends "accounts/base.html" %} {% load i18n %} {% load crispy_forms_tags %}

<!--Block Header-->
{% block head_title %} {% translate "Sign In" %} {% endblock head_title %}

<!--Block Content-->
{% block content %}
<div class="container">
  <div class="row h-100 justify-content-center align-items-center">
    <div class="col-md-4 mt-5">
      <div class="card shadow-md mt-5">
        <div class="card-header text-center" style="background-color: #02474c">
          <legend style="color: #ffffff">Welcome Back,</legend>
          <h6 style="color: #ffffff">sign in to continue</h6>
        </div>

        <div class="card-body">
          <form
            method="POST"
            action="{% url 'accounts:login' %}"
            enctype="multipart/form-data"
          >
            {%csrf_token%} {{form|crispy}}
            <!-- 2 column grid layout for inline styling -->
            <div class="row mb-4">
              <div class="col d-flex justify-content-center">
                <!-- Checkbox -->
                <div class="form-check">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    value=""
                    id="form2Example31"
                    checked
                  />
                  <label class="form-check-label" for="form2Example31">
                    Remember me
                  </label>
                </div>
              </div>

              <div class="col">
                <!-- Simple link -->
                <a href="{%url 'accounts:password_reset'%}">Forgot password?</a>
              </div>
            </div>

            <!-- Submit button -->
            <button
              type="submit"
              class="btn btn-outline-primary col-md-12 btn-block mb-4"
            >
              Sign in
            </button>

            <!-- Register buttons -->
            <div class="text-center">
              <p>
                Don't have an account?
                <a href="{%url 'accounts:signup'%}">Register Here</a>
              </p>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</div>
{% endblock content %}
```

![LoginScreen](https://github.com/qinyanjuidavid/supreme-eureke/assets/49823575/4a57ec60-ae67-4e39-aaeb-27f41eca86e4)

###### home.html

- The home.html template also extends base.html and represents the home page of the application. It includes a navigation bar block and a table displaying information about users.
- The table showcases user details such as email, name, phone number, role, date joined, and status indicators for activity and superuser status.
- The template provides a visually appealing and informative view for users after they log in.

```html
{% extends "accounts/base.html" %} {% load i18n %}

<!--Block Header-->
{% block head_title %} {% translate "Home" %} {% endblock head_title %} {% block
navBar %} {% include 'includes/navbar.html' %} {% endblock %}

<!--Block content-->
{% block content %}
<div class="container">
  <div class="jumbotron mt-4">
    <legend class="mt-3" align="left">List of users</legend>
    <table class="table table-striped table-bordered">
      <tr>
        <thead class="text-white" style="background-color: #02474c">
          <th>#</th>
          <th>Email address</th>
          <th>Name</th>
          <th>Phone number</th>
          <th>Role</th>
          <th>Date joined</th>
          <th>Active</th>
          <th>Superuser</th>
        </thead>
      </tr>
      {% if users %} {% for user in users %}
      <tr>
        <td>{{ forloop.counter }}.</td>
        <td>{{ user.email }}</td>
        <td>{{ user.name }}</td>
        <td>{{ user.phone_no|default:"" }}</td>
        <td>{{ user.role }}</td>
        <td>{{ user.timestamp }}</td>
        <td>
          {% if user.is_active %}
          <i class="fa fa-check fa-md text-success"></i>
          {% else %}
          <i class="fa fa-times fa-md text-danger"></i>
          {% endif %}
        </td>
        <td>
          {% if user.is_superuser or user.role == "SUPERUSER" %}
          <i class="fa fa-check fa-md text-success"></i>
          {% else %}
          <i class="fa fa-times fa-md text-danger"></i>
          {% endif %}
        </td>
      </tr>
      {% endfor %} {% else %}
      <!-- Display an empty row if there are no users -->
      <tr>
        <td colspan="8">No users available</td>
      </tr>
      {% endif %}
    </table>
  </div>
</div>
{% endblock content %}
```

![successScreen](https://github.com/qinyanjuidavid/supreme-eureke/assets/49823575/ffd05264-72dd-4ea7-81f9-9e35fc3b62a9)
