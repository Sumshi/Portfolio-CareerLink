
<h1>CareerLink</h1>
<h2><i>Discover Exciting Opportunities</i></h2>
<hr>
CareerLink

<hr>
<h3>Introduction</h3>
<p>
    Welcome to CareerLink, a premier job posting platform designed to connect talented individuals with exciting career opportunities. This platform has been meticulously developed as part of a comprehensive project, showcasing expertise and innovation in the field of job searching and career development.
</p>
<p>
    CareerLink offers a user-friendly experience, allowing individuals to explore job listings, apply for positions, and stay informed about the latest career trends and opportunities. Users can dive into a dynamic and engaging community, sharing insights and experiences to foster professional growth.
</p>
<h3>Technology Stack</h3>
<p>
    <h4>Frontend: </h4>
        <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>JavaScript</li>
        </ul>
</p>
<p>
    <h4>Backend:</h4>
        <ul>
            <li>Jinja Flask</li>
            <li>Python</li>
        </ul>
</p>
<p>
    <h4>Hosting and Devops</h4>
    <ul>
        <li>Digital Ocean server for hosting</li>
        <li>Nginx web server for handling HTTP requests</li>
        <li>Gunicorn application server for serving Flask application</li>
        <li>Certbot for SSL encryption</li>
        <li>UFW firewall for security</li>
    </ul>
</p>
<p>
    <h4>Database:</h4>
    <ul>
        <li>MYSQL: Main database system for storing and managing data</li>
        <li>Alembic: For database Migration</li>
    </ul>
</p>
<h3>Architecture</h3>
<p>
    The architecture of CareerLink is carefully crafted, considering the best approach to provide a seamless user experience. The project began with the development of static pages, allowing for a clear visualization of the front-end, which, in turn, facilitated the back-end development process.
</p>

<p>
    <h4>Configuration</h4>
    <ol>
        <li><strong>alembic: </strong>Contains database migration scripts</li>
        <li><strong>Forms.py: </strong>Contains Flask forms for handling user input across the application</li>
        <li><strong>app.py: </strong>Main application module for my Flask application. Sets up Flask and provides utility for Flask shell</li>
    </ol>
</p>
<h4>Application Logic (Models Folder)</h4>
<ol>
    <li><strong>Python Modules:</strong>
        <ul>
            <li><strong>jobs.py:</strong> Manages job-related logic, including functionalities such as job creation, editing, and deletion.</li>
            <li><strong>application.py:</strong> Defines application process and defined inputs.</li>
            <li><strong>base_model.py:</strong> Provides Flask forms for handling user input across the application.</li>
            <li><strong>__init__.py:</strong> Marks the 'app' directory as a Python package, facilitating modular organization and importability.</li>
            <li><strong>job_history.py:</strong> Defines database models related to job history, capturing historical data or changes related to jobs.</li>
            <li><strong>recruiter.py:</strong> Handles views specific to recruiters, managing their interactions with the platform.</li>
            <li><strong>jobseeker.py:</strong> Handles views specific to job seekers, handling their interactions and experiences on the platform.</li>
        </ul>
    </li>
</ol>


<h4>Application Logic (web_static/templates Folder)</h4>
<ol>
    <li><strong>static and templates:</strong> Flask uses the 'static' folder to serve static assets (CSS, JS, and images) and the 'templates' folder for HTML templates.</li>
    <li>Main static files that power our application</li>
    <ul>
        <li><strong>application_form.html:</strong> Provides the application form for user inputs.</li>
        <li><strong>403.html:</strong> Custom error page for forbidden access.</li>
        <li><strong>404.html:</strong> Custom error page for page not found.</li>
        <li><strong>500.html:</strong> Custom error page for internal server errors.</li>
        <li><strong>about.html:</strong> Page providing information about the application or the team behind it.</li>
        <li><strong>applied_jobs.html:</strong> Displays a list of jobs to which a user has applied.</li>
        <li><strong>contact.html:</strong> Page with contact information or a form for user inquiries.</li>
        <li><strong>job_history.html:</strong> Presents a user's job application history.</li>
        <li><strong>job_posting_form.html:</strong> Form for recruiters to post new job opportunities.</li>
        <li><strong>job_details.html:</strong> Displays detailed information about a specific job posting.</li>
        <li><strong>joblists.html:</strong> Lists available job opportunities.</li>
        <li><strong>logIn.html:</strong> User login page.</li>
        <li><strong>recruiter_signup.html:</strong> Signup form for recruiters.</li>
        <li><strong>posted_jobs.html:</strong> Displays jobs posted by a recruiter.</li>
        <li><strong>userDashboard.html:</strong> Dashboard for registered users.</li>
        <li><strong>headerContent.html:</strong> Common header content for various pages.</li>
        <li><strong>jobseekerProfile.html:</strong> Displays the profile of a job seeker.</li>
        <li><strong>recruiterProfile.html:</strong> Displays the profile of a recruiter.</li>
        <li><strong>recruiterDashboard.html:</strong> Dashboard for recruiters.</li>
        <li><strong>jobseeker_signup.html:</strong> Signup form for job seekers.</li>
        <li><strong>recruiterProfile_backup.html:</strong> A backup or alternative version of the recruiter profile page.</li>
    </ul>
</ol>



<p>
    <h4>Testing</h4>
    <ul>
         <li><strong>tests.py: </strong>Test cases for the Flask application</li>
    </ul>
</p>

<h3>Getting Started</h3>
<p>
    To set up and run the CareerLink project locally, follow these steps:
    <ol>
        <li>Clone the repository</li>
        <li>Navigate to the project directory</li>
        <li>Install the required dependencies</li>
        <li>Run the Flask application</li>
            <em>flask run or flask run --debug</em>
        <li>Access the application</li>
            <em>http://127.0.0.1:5000/</em>
    </ol>
</p>
<p>
   Now you have the CareerLink project up and running locally. Feel free to explore, make changes, and contribute to the project! 
</p>
<h3>Deployment and Hosting</h3>
<p>
    CareerLink is hosted on a .tech domain. Purchase a domain name on .tech and add A records pointing to your server's IP address.
</p>
<p>
    CareerLink was deployed on a Digital Ocean server. Follow these steps for deployment.
    <ol>
        <li>Set up a Digital Ocean Droplet:
            <ul>
                <li>Create a new droplet</li>
                <li>Choose a distribution (e.g., Ubuntu)</li>
                <li>Set up SSH access and log in to your Droplet from your local terminal</li>
                <li>Create a less privileged user and give them sudo privileges</li>
                <li>Set up SSH for the user by adding your public key into .ssh</li>
                <li>Exit and SSH into the droplet as the less privileged user</li>
            </ul>
        </li>
        <li>Secure your server with UFW</li>
        <li>Clone the repository</li>
        <li>Navigate to the project directory</li>
        <li>Install dependencies</li>
        <li>Configure the application</li>
        <li>Install, set up MYSQL and upgrade the database</li>
        <li>Install and configure Nginx</li>
        <li>Install and configure Gunicorn </li>
        <li>Setup SSL with Certbot</li>
        <li>Visit your domain</li>        
    </ol>
</p>
<h3>Acknowledgments</h3>
<h4>Resources: </h4>
<p>
    <ol>
        <li><a href="https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world">The Flask Mega Tutorial</a></li>
        <li><a href="https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04">Digital Ocean Gunicorn installation</a></li>
        <li><a href="https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-22-04">Digital Ocean Nginx installation</a></li>
        <li><a href="https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-22-04">Digital Ocean Server setup</a></li>
        <li><a href="https://flask.palletsprojects.com/en/3.0.x/">Flask Documentation</a></li>
        <li>chatGPT</li>
    </ol>
</p>
<p>
    I want to express my gratitude to the following individuals who greatly contributed to the development of the CareerLink project:
</p>
<p>
    <ol>
        <li>Collaborator, <a href="https://github.com/Bulimo">Eric Ubaga</a>,
            played a pivotal role in the backend development, contributing to server setup, providing crucial support, and offering valuable corrections. I extend my heartfelt gratitude for his guidance and expertise, which were instrumental in overcoming challenges and enhancing the overall success of the CareerLink project.</li>
        <li>Collaborator, <a href="https://github.com/XimeonLeo">Simeon Leo</a>,
            specialized in MySQL integration and presentation design. His expertise in these areas significantly contributed to the project's success.</li>
        <li>I want to acknowledge the <a href="https://www.alxafrica.com/">ALX</a>
            community and the wider community of developers and contributors whose open-source projects, discussions, and code snippets served as a source of inspiration and learning.</li>
    </ol>
</p>
<p><em><i class="fa-solid fa-heart"></i>Thank You all</p></em>
</p>