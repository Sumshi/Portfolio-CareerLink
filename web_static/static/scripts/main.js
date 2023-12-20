// const jobs = [
//     {
//         title: "Senior Backend Engineer ",
//         image: "../static/images/SE.svg",
//         details:
//             "Responsible for designing, developing and maintaining software systems and applications.",
//         openPositions: "2",
//         link: "https://www.linkedin.com/jobs/view/3710552708/?eBP=CwEAAAGMEa-NKRbhgnP2VmXmbRCEAi4r48jA6Uwq2RUNnrjGYMuwfu96sxZ3nDMFWdaMLBRI0vSbfQe8CN_bp94H02CdIUrt7O3LARwRMZa827ivIfUh5CM25joxgEg36KApbhNpF8Feh-v0XKan7ZGtbo43Mxa1ujMnbihEKHZinmSjpEwEO5rnj2EtuMA6bG49Vqq_85pFZxyqv11kw1BtqZv7m8Hn1bMLPgivSp6qoCV0hOOhbjWL7FqalnonJUbn-3VUhS2cTyHnFzanqBaTWUHVpDBd0MCfvJ38lgzk7H9VdLeXzZLJn_cm96k6agjx7l_mt1nzqnPNfCH4mqYawaVoQ5NUob8KBJm02DTRbxGWEhWJgIftRSFEQKLpTDk51FTiSpkk&refId=H2oh%2BIwa1IFBtAneO5Eycg%3D%3D&trackingId=sxKlZYtOEWguGIXlyGPXbw%3D%3D&trk=flagship3_search_srp_jobs",
//     },

//     {
//         title: "Junior Data Analyst",
//         image: "../static/images/data.svg",
//         details:
//             "Responsible for collecting, analyzing and interpreting large data sets to help organizations make better decisions.",
//         openPositions: "3",
//         link: "https://www.linkedin.com/jobs/view/3765730486/?alternateChannel=search&refId=a0ba3ee7-0660-4c48-9141-9398e47ff1ed&trackingId=l3FJBkuMRJC4mi3QDI7AWA%3D%3D",
//     },

//     {
//         title: "Project Manager",
//         image: "../static/images/manager.svg",
//         details:
//             "Responsible for planning, executing and closing projects on time and within budget.",
//         openPositions: "1",
//         link: "https://www.linkedin.com/jobs/view/3766363465/?alternateChannel=search&refId=3tHLUTceypWK3BlasxnXkw%3D%3D&trackingId=w6qO5CKVZ9OYkNSVPw5rvQ%3D%3D&trk=d_flagship3_search_srp_jobs",
//     },

//     {
//         title: "Information Technology Senior",
//         image: "../static/images/lecturer.svg",
//         details:
//             "Develop and execute the organizations IT strategy in alignment with its business goals and objectives.",
//         openPositions: "1",
//         link: "https://www.linkedin.com/jobs/view/3769972768/?alternateChannel=search&refId=addc77ab-ca93-4893-b956-639e607677c0&trackingId=UywaxCFhQkif1SpkoSdKFg%3D%3D",
//     },

//     {
//         title: "Sales Representative",
//         image: "../static/images/sales.svg",
//         details:
//             "Responsible for reaching out to potential customers and closing sales deals.",
//         openPositions: "4",
//         link: "https://www.linkedin.com/jobs/view/3727766609/?alternateChannel=search&refId=vahEqNYabW1rh8CUuPj8Bw%3D%3D&trackingId=HXaXC6lm6RrIzfQmsNcRNA%3D%3D&trk=d_flagship3_search_srp_jobs",
//     },

//     {
//         title: "Legal Secretary",
//         image: "../static/images/lawyer.svg",
//         details:
//             "The position supports attorneys with specific client matters and a variety of practice groups by processing work in an efficient and accurate manner.",
//         openPositions: "1",
//         link: "https://www.linkedin.com/jobs/view/3756935405/?alternateChannel=search&refId=ne5PVJd0NRdIgAygPsyjag%3D%3D&trackingId=Q3%2FXsz%2BacpoaI2%2BMBY6Ynw%3D%3D&trk=d_flagship3_search_srp_jobs",
//     },

//     {
//         title: "Data Centre Mechanical Engineer",
//         image: "../static/images/electrical.svg",
//         details:
//             "Integrate design requirements as defined by client, structure design and architecture design as well as specialists to compile requirements for bid High Level Designs (HLD).",
//         openPositions: "1",
//         link: "https://www.linkedin.com/jobs/view/3758907963/?alternateChannel=search&refId=nADkGxeQNIk7NSRYpopSTg%3D%3D&trackingId=dOzz9gKB0qd8Lq1RBgO14g%3D%3D&trk=d_flagship3_search_srp_jobs",
//     },

//     {
//         title: "Nurse",
//         image: "../static/images/medicine-bottle-svgrepo-com.svg",
//         details:
//             "Nurses play a crucial role in the healthcare system, providing a wide range of services to promote and maintain the health and well-being of patients.",
//         openPositions: "3",
//         link: "https://www.linkedin.com/jobs/view/3766287805/?alternateChannel=search&refId=c4pJKZOX33T797yFd7SwsQ%3D%3D&trackingId=Ac3YuC7LBaY%2F%2FbmbJa7DfA%3D%3D&trk=d_flagship3_search_srp_jobs",
//     },
//     {
//         title: "Accountant",
//         image: "../static/images/accountant.svg",
//         details:
//             "Manage financial records, prepare and analyze financial statements, ensure compliance with accounting standards, and provide valuable insights for strategic decision-making. Stay updated on relevant financial regulations and contribute to the financial health of the organization.",
//         openPositions: "1",
//         link: "https://www.linkedin.com/jobs/view/3694160606/?alternateChannel=search&refId=tVD0Qe16t4LEBNvJkmeIIQ%3D%3D&trackingId=nPy4lzPKDdyDU%2Byf4%2FQnFA%3D%3D&trk=d_flagship3_search_srp_jobs",
//     },

// ];
function mainJSFunction(jobs) {

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

                let title = document.createElement("h3");
                title.innerHTML = job.title;
                title.classList.add("job-title");

                let details = document.createElement("div");
                if (job.role) {
                    details.innerHTML = job.role;
                    details.classList.add("details");
                    console.log("Added job.role")
                } else {
                    details.innerHTML = "Role information not available";
                    details.classList.add("details");
                    console.log('No role information available')
                }

                let detailsBtn = document.createElement("a");
                detailsBtn.href = `/job/${job.id}`;
                detailsBtn.innerHTML = "More Details";
                detailsBtn.classList.add("details-btn");

                let open_position = document.createElement("p");
                open_position.classList.add("open-positions");

                if (job.open_position == 1) {
                    open_position.innerHTML = `${job.open_position} open position`;
                } else {
                    open_position.innerHTML = `${job.open_position} open positions`;
                }

                jobCard.appendChild(title);
                jobCard.appendChild(details);
                jobCard.appendChild(open_position);
                jobCard.appendChild(detailsBtn);

                jobsContainer.appendChild(jobCard);
            }
        });
    };

    createJobListingCards();

    jobSearch.addEventListener("input", (e) => {
        searchTerm = e.target.value;

        createJobListingCards();
    });
}
