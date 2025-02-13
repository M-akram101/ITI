import React from "react";

export function Header(props) {
  return (
    <div className="d-flex justify-content-between align-items-center bg-dark p-3 text-white">
      <h2>Product List</h2>
      <button onClick={props.onHide} className="btn btn-danger">
        Hide Products
      </button>
    </div>
  );
}
