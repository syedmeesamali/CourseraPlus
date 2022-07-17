const startBtn = document.getElementById('start-btn')
const output = document.getElementById('input-box')
startBtn.addEventListener('click', makeRun)

//Array to perform filter and update for premium products
let products = [
    {prodName: 'Gucci perfume', price: 300}, 
    {prodName: 'Gucci Belt', price: 250},
    {prodName: 'Gucci Belt', price: 450},
    {prodName: 'Smiley shirt', price: 350},
    {prodName: 'Smiley T-shirt', price: 250},
    {prodName: 'Prime 21', price: 270},
    {prodName: 'One million 350ml', price: 650}
];


const prem = products.filter(product => product.price > 300)
.map(product => {
    return {
        prodName: product.prodName.toUpperCase(),
        price: product.price
    }
}).reduce((stocks, currentProd) => {
    let stockItem = stocks.find(product => product.prodName === currentProd.prodName);
    if(stockItem)
        ++stockItem.stock;
    else
        stocks.push({
            prodName: currentProd.prodName,
            stock: 1
        })
    return stocks;
}, []);


//RUN Functions
function makeRun()
{    
    console.log(products)
    output.append('>>> Premium products' + '\n\n' + prem + '\n\n')
    console.log(prem)
    //output.append('>>> Stock Value' + '\n\n' + prodStock + '\n\n')
    //console.log(prodStock)
}