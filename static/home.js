// JavaScript code for handling search functionality
const searchButton = document.getElementById("search-button");
const bookSearchInput = document.getElementById("book-search");

searchButton.addEventListener("click", () => {
    const searchTerm = bookSearchInput.value.trim();
    if (searchTerm !== "") {
        // Perform the search operation (you can define this functionality)
        alert(`Searching for: ${searchTerm}`);
    }
});
