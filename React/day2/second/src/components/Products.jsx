import React from "react";
import ProductCard from "./ProductCard.jsx";

export function Product() {
  let products = [
    {
      id: 1,
      name: "Alpharomeo",
      price: "100,000$",
      category: "Sedan",
      quantity: 10,
      description: "A stylish and powerful sedan with Italian craftsmanship.",
    },
    {
      id: 2,
      name: "Lamborghiny",
      price: "500,000$",
      category: "SUV",
      quantity: 1,
      description: "A luxury SUV with top-tier performance and bold design.",
    },
    {
      id: 3,
      name: "Volvo",
      price: "100,000$",
      category: "SubCompact",
      quantity: 0,
      description: "A safe and reliable subcompact car with great efficiency.",
    },
    {
      id: 4,
      name: "BMW",
      price: "250,000$",
      category: "Sedan",
      quantity: 5,
      description:
        "A premium sedan with a perfect balance of luxury and sportiness.",
    },
  ];

  return (
    <div className="bg-primary p-5 text-dark">
      <div className="container">
        <div className="row">
          {products.map((product) => (
            <div key={product.id} className="col-md-3 col-sm-6 mb-4">
              <ProductCard product={product} />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
