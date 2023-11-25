const jobs = [
    {
        title: "Software Engineer",
        image: "../static/images/software-engineer.svg",
        details:
            "Responsible for designing, developing and maintaining software systems and applications.",
        openPositions: "2",
        link: "#",
    },

    {
        title: "Data Scientist",
        image: "../static/images/data-scientist.svg",
        details:
            "Responsible for collecting, analyzing and interpreting large data sets to help organizations make better decisions.",
        openPositions: "3",
        link: "#",
    },

    {
        title: "Project Manager",
        image: "../static/images/project-manager.svg",
        details:
            "Responsible for planning, executing and closing projects on time and within budget.",
        openPositions: "1",
        link: "#",
    },

    {
        title: "Product Manager",
        image: "../static/images/product-manager.svg",
        details:
            "Responsible for managing the entire product life cycle, from ideation to launch and post-launch maintenance.",
        openPositions: "1",
        link: "#",
    },

    {
        title: "Sales Representative",
        image: "../static/images/sales-representative.svg",
        details:
            "Responsible for reaching out to potential customers and closing sales deals.",
        openPositions: "4",
        link: "#",
    },

    {
        title: "Marketing Manager",
        image: "../static/images/marketing-manager.svg",
        details:
            "Responsible for creating and executing marketing strategies to promote a company or product.",
        openPositions: "1",
        link: "#",
    },
];

const jobsHeading = document.querySelector(".jobs-list-container h2");
const jobsContainer = document.querySelector(".jobs-list-container .jobs");
const jobSearch = document.querySelector(".jobs-list-container .job-search");

let searchTerm = "";

if (jobs.length == 1) {
    jobsHeading.innerHTML = `${jobs.length} Job`;
} else {
    jobsHeading.innerHTML = `${jobs.length} Jobs`;
}

const createJobListingCards = () => {
    jobsContainer.innerHTML = "";

    jobs.forEach((job) => {
        if (job.title.toLowerCase().includes(searchTerm.toLowerCase())) {
            let jobCard = document.createElement("div");
            jobCard.classList.add("job");

            let image = document.createElement("img");
            image.src = job.image;

            let title = document.createElement("h3");
            title.innerHTML = job.title;
            title.classList.add("job-title");

            let details = document.createElement("div");
            details.innerHTML = job.details;
            details.classList.add("details");

            let detailsBtn = document.createElement("a");
            detailsBtn.href = job.link;
            detailsBtn.innerHTML = "More Details";
            detailsBtn.classList.add("details-btn");

            let openPositions = document.createElement("span");
            openPositions.classList.add("open-positions");

            if (job.openPositions == 1) {
                openPositions.innerHTML = `${job.openPositions} open position`;
            } else {
                openPositions.innerHTML = `${job.openPositions} open positions`;
            }

            jobCard.appendChild(image);
            jobCard.appendChild(title);
            jobCard.appendChild(details);
            jobCard.appendChild(detailsBtn);
            jobCard.appendChild(openPositions);

            jobsContainer.appendChild(jobCard);
        }
    });
};

createJobListingCards();

jobSearch.addEventListener("input", (e) => {
    searchTerm = e.target.value;

    createJobListingCards();
});
