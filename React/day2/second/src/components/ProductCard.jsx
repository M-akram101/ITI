import React, { useState } from "react";

export default function ProductCard({ product }) {
  let buttonColor = "btn-success";
  if (product.quantity === 1) {
    buttonColor = "btn-warning";
  } else if (product.quantity === 0) {
    buttonColor = "btn-danger";
  }

  const [isExpanded, setIsExpanded] = useState(false);

  const toggleDescription = () => {
    setIsExpanded(!isExpanded);
  };

  const shortDescription = product.description.slice(0, 25) + "...";

  return (
    <div className="border border-dark rounded p-3 h-100 d-flex flex-column">
      <h2 className="fs-5">Product: {product.name}</h2>
      <p className="fs-5">Price: {product.price}</p>
      <h2 className="fs-5">Quantity: {product.quantity}</h2>
      <h2 className="fs-5">Category: {product.category}</h2>

      <img
        src={`/images/${product.name.toLowerCase()}.jpg`}
        alt={product.name}
        style={{ width: "100%", height: "auto" }}
      />

      <p className="mt-2">
        {isExpanded ? product.description : shortDescription}
      </p>

      <button className="btn btn-link p-0" onClick={toggleDescription}>
        {isExpanded ? "Show Less" : "Show More"}
      </button>

      <button
        className={`btn ${buttonColor} mt-auto`}
        disabled={product.quantity === 0}
      >
        Buy Now
      </button>
    </div>
  );
}
