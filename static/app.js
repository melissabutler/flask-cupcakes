const BASE_URL = "http://127.0.0.1:5000/api"

function generateCupcakeHTML(cupcake){
    return `
    <div data-cupcake-id={cupcake.id}>
    <li> ${cupcake.flavor}/ ${cupcake.size} / ${cupcake.rating}
    </li>
    <img class="cupcake-img" src=${cupcake.image}">
    </div>`;

}

async function showInitialCupcakes() {
    const response = await axios.get(`${BASE_URL}/cupcakes`);

    for(let cupcake of response.data.cupcakes){
        let newCupcake = $(generateCupcakeHTML(cupcake));
        $("#cupcakes-list").append(newCupcake);
    }
}

$("#new-cupcake-form").on("submit", async function(evt){
    evt.preventDefault()
    let flavor = $("#form-flavor").val();
    let size = $("#form-size").val();
    let rating = $("#form-rating").val();
    let image = $("#form-image").val();

    const response = await axios.post(`${BASE_URL}/cupcakes`, {
        flavor, rating, size, image
    });

    let newCupcake = $(generateCupcakeHTML(response.data.cupcake));
    $("#cupcakes-list").append(newCupcake);
    $("#new-cupcake-form").trigger('reset');

});


showInitialCupcakes();