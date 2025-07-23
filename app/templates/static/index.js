// function AddToWishlist() {
//     const submit = document.getElementById('AddToWishList')
//     submit.addEventListener("submit", function () {
//         const wishlist_url = "/movie/add";
//         let data = new FormData();
//         imdb_id = getElementById("staticid");
//         movie_name = getElementById('staticname');
//         movie_geners = getElementById('staticgeners');
//         movie_lan = getElementById('staticlanguages');
//         movie_dir = getElementById('staticdirector');
//         movie_rating = getElementById('staticrating');
//         movie_url = getElementById('staticurl');
//         console.log(imdb_id + movie_name)
//     });
// }
const submit = document.getElementById('AddToWishList')
submit.addEventListener("click", function () {
    const wishlist_url = "/movie/add";
    let data = new FormData();
    imdb_id = document.getElementById("staticid").value;
    movie_name = document.getElementById('staticname').value;
    movie_geners = document.getElementById('staticgeners').value;
    movie_lan = document.getElementById('staticlanguages').value;
    movie_dir = document.getElementById('staticdirector').value;
    movie_rating = document.getElementById('staticrating').value;
    movie_url = document.getElementById('staticurl').value;
    data.append('imdb_id',imdb_id);
    data.append('name',movie_name);
    data.append('geners',movie_geners);
    data.append('lan',movie_lan);
    data.append('dir',movie_dir);
    data.append('rating',movie_rating);
    data.append('url',movie_url)
    console.log(data)
});