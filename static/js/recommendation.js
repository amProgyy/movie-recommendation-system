
const recommendationForm =
    document.getElementById("recommendation-form");

const movieInput =
    document.getElementById("movie-input");

const recommendationContainer =
    document.getElementById("recommendation-container");

const loading =
    document.getElementById("loading");

const errorMessage =
    document.getElementById("error-message");


recommendationForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    const movieName = movieInput.value.trim();

    if (!movieName) {
        errorMessage.textContent = "Please enter a movie name.";
        errorMessage.style.display = "block";
        return;
    }

    loading.style.display = "block";
    errorMessage.style.display = "none";

    try {

        const response = await fetch("/recommend", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                movie: movieName,
                no_of_movies: 5
            })
        });


        const data = await response.json();

        console.log("Backend response:", data);


        if (!response.ok) {

            throw new Error(
                data.detail || "Failed to get recommendations"
            );
        }


        loading.style.display = "none";


        // Clear previous cards
        recommendationContainer.innerHTML = "";


        const recommendations = data.recommendation;


        console.log("Recommendations:", recommendations);


        if (!recommendations || recommendations.length === 0) {

            recommendationContainer.innerHTML = `
                <div class="empty-message">
                    <p>No recommendations found.</p>
                </div>
            `;

            return;
        }


        // Create movie cards
        recommendations.forEach(function (movie) {

            console.log("Movie:", movie);
            console.log("Title:", movie.title);


            const movieCard = document.createElement("div");

            movieCard.classList.add("movie-card");


            movieCard.innerHTML = `
                <h3>${movie.title}</h3>

                <p>
                    Similarity:
                    ${(movie.similarity * 100).toFixed(1)}%
                </p>
            `;


            recommendationContainer.appendChild(movieCard);

        });


        movieInput.value = "";


    } catch (error) {

        console.error("Error:", error);

        loading.style.display = "none";

        errorMessage.textContent = error.message;

        errorMessage.style.display = "block";
    }

});

