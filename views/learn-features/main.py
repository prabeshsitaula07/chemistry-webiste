import os

# HTML content to replace existing content
new_html_content = """

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
    <title>Sandmayer Reaction</title>
</head>

<body>

    <%- include('../../layout') %>

        <style>
            .back-btn button {
                margin: 40px;
                height: 50px;
                width: 120px;
                border-radius: 12px;
                color: red;
            }

            .back-btn button:hover {
                background: darkgray;
            }

            .card-body p{
                color: black;
            }
        </style>

        <a href="../naming-reaction" class="back-btn"><button><--Back</button></a>
        <div class="container" id="mainContainer">
            <div class="accordion" id="accordionSections">

                <!-- General Reaction Section -->
                <div class="card" id="cardGeneralReaction">
                    <div class="card-header" id="headingGeneralReaction">
                        <h2 class="mb-0">
                            <button class="btn btn-link" type="button"
                                onclick="toggleSection('collapseGeneralReaction')">
                                ▼ General Reaction
                            </button>
                        </h2>
                    </div>

                    <div id="collapseGeneralReaction" class="collapse show" aria-labelledby="headingGeneralReaction">
                        <div class="card-body">
                            <!-- Your content for General Reaction goes here -->
                            <p>General reaction hune container ho yo. Lorem ipsum, dolor sit amet consectetur
                                adipisicing elit. Vero illum nostrum fugiat vitae vel maiores distinctio eos similique,
                                quaerat ea.</p>
                        </div>
                    </div>
                </div>

                <!-- Description Section -->
                <div class="card" id="cardDescription">
                    <div class="card-header" id="headingDescription">
                        <h2 class="mb-0">
                            <button class="btn btn-link" type="button" onclick="toggleSection('collapseDescription')">
                                ▶ Description
                            </button>
                        </h2>
                    </div>

                    <div id="collapseDescription" class="collapse" aria-labelledby="headingDescription">
                        <div class="card-body">
                            <!-- Your content for Description goes here -->
                            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Deserunt odit omnis asperiores
                                libero voluptatum doloribus neque quod, numquam voluptate facere assumenda laboriosam
                                ipsam vitae hic qui, expedita voluptas dolor. Voluptatem iste, sunt a minima nostrum
                                distinctio facere! Ab magni eum vitae? Eaque quibusdam maxime aspernatur minima natus
                                eveniet! Consequatur, corporis.</p>
                        </div>
                    </div>
                </div>

                <!-- Example Section -->
                <div class="card" id="cardExample">
                    <div class="card-header" id="headingExample">
                        <h2 class="mb-0">
                            <button class="btn btn-link" type="button" onclick="toggleSection('collapseExample')">
                                ▶ Example
                            </button>
                        </h2>
                    </div>

                    <div id="collapseExample" class="collapse" aria-labelledby="headingExample">
                        <div class="card-body">
                            <!-- Your content for Example goes here -->
                            <p>Here is an example of the Sandmayer Reaction...</p>
                        </div>
                    </div>
                </div>

                <div class="card" id="cardApplicationIOC">
                    <div class="card-header" id="headingApplicationIOC">
                        <h2 class="mb-0">
                            <button class="btn btn-link" type="button"
                                onclick="toggleSection('collapseApplicationIOC')">
                                ▶ Application In Organic Chemistry
                            </button>
                        </h2>
                    </div>

                    <div id="collapseApplicationIOC" class="collapse" aria-labelledby="headingApplicationIOC">
                        <div class="card-body">
                            <!-- Your content for Example goes here -->
                            <p>The 2,4-DNP test is commonly used in organic chemistry laboratories for the
                                identification of aldehydes and ketones. It provides a simple and quick means of
                                determining whether a given compound contains a carbonyl group.</p>
                        </div>
                    </div>
                </div>

                <div class="card" id="cardModernApplication">
                    <div class="card-header" id="headingModernApplication">
                        <h2 class="mb-0">
                            <button class="btn btn-link" type="button"
                                onclick="toggleSection('collapseModernApplication')">
                                ▶ Modern Application
                            </button>
                        </h2>
                    </div>

                    <div id="collapseModernApplication" class="collapse" aria-labelledby="headingModernApplication">
                        <div class="card-body">
                            <!-- Your content for Example goes here -->
                            <p>Despite its historical significance, the 2,4-DNP test is less commonly used in modern
                                analytical chemistry due to the availability of more advanced instrumental techniques,
                                such as nuclear magnetic resonance (NMR) and mass spectrometry, which offer greater
                                sensitivity and specificity in identifying and characterizing organic compounds.</p>
                        </div>
                    </div>
                </div>

                <!-- History Section -->
                <div class="card" id="cardHistory">
                    <div class="card-header" id="headingHistory">
                        <h2 class="mb-0">
                            <button class="btn btn-link" type="button" onclick="toggleSection('collapseHistory')">
                                ▶ History
                            </button>
                        </h2>
                    </div>

                    <div id="collapseHistory" class="collapse" aria-labelledby="headingHistory">
                        <div class="card-body">
                            <!-- Your content for History goes here -->
                            <p> 2,4-Dinitrophenylhydrazine was first synthesized by the German chemist Emil Fischer in
                                the late 19th century. Fischer, who was awarded the Nobel Prize in Chemistry in 1902 for
                                his work on sugars and purines, developed the 2,4-DNP reagent as part of his broader
                                research on organic compounds. <br>
                                The 2,4-DNP test as a method for identifying carbonyl compounds was later developed by
                                Russian chemist Nikolay Zelinsky in the early 20th century. Zelinsky is known for his
                                contributions to the fields of organic and physical chemistry. The test became widely
                                used as a qualitative test for the presence of carbonyl groups in organic compounds.</p>
                                <br><a href="https://www.sciencedirect.com/topics/neuroscience/2-4-dinitrophenol" target="_blank">Learn More</a>
                        </div>
                    </div>
                </div>

            </div>
        </div>

        <footer class="footer mt-auto py-3" style="
  background: linear-gradient(45deg, darkblue, lightblue, transparent);
  ">

            <div class="container text-center">
                <div class="row">
                    <div class="col-md-4">
                        <h5>About Us</h5>
                        <p>Your go-to resource for Grade 11 and 12 Organic Chemistry, providing comprehensive learning
                            materials and resources to help students excel in their chemistry studies.</p>
                    </div>
                    <div class="col-md-4">
                        <h5>Quick Links</h5>
                        <ul class="list-unstyled">
                            <li><a href="/">Home</a></li>
                            <li><a href="/about">About</a></li>
                            <li><a href="/learn">Learn</a></li>
                            <li><a href="/blog">Blog</a></li>
                            <li><a href="/contact">Contact</a></li>
                        </ul>
                    </div>
                    <div class="col-md-4">
                        <h5>Contact Us</h5>
                        <p>Email: sitaulaprabesh07@gmail.com<br>Phone: +977 9848589357</p>
                        <a href="https://prabeshsitaula.com.np/" target="_blank">Prabesh Sitaula</a>
                    </div>
                </div>
                <hr>
                <p class="text-muted">� 2023 My Chemistry Website. All rights reserved.</p>
                <div class="row mt-4">
                    <div class="col-md-12">
                        <h5>Advertise with Us</h5>
                        <p>Place your advertisement content here.</p>
                    </div>
                </div>
            </div>
        </footer>
        <script src="../../script.js"></script> <!-- Assuming your script.js is in the parent directory -->

        <script>
            function toggleSection(sectionId) {
                const section = document.getElementById(sectionId);
                section.classList.toggle('show');
            }
        </script>

        <style>
            .card {
                height: fit-content;
                margin-top: 10px;
                border: 1px solid grey !important;
                border-radius: 10px !important;
            }

            .btn-link {
                text-decoration: none !important;
            }

            /* .accordion>.card:not(:last-of-type) {
} */
        </style>
</body>

</html>


"""


# Function to replace content in all existing files
# Modify the replace_content_in_files function
def replace_content_in_files(directory_path, file_extension='.ejs'):
    try:
        # Get a list of all files with the specified extension in the current directory
        files = [file for file in os.listdir(directory_path) if file.endswith(file_extension)]

        # Print debug information
        print(f"Files to process: {files}")

        # Iterate through each file and replace its content with the new HTML content
        for file_name in files:
            file_path = os.path.join(directory_path, file_name)
            print(f"Processing file: {file_path}")
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_html_content)

    except Exception as e:
        # Print the error message for debugging
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace "." with the actual path to your project if the files are not in the same directory as the script
    replace_content_in_files("./views/learn-features/reactions")