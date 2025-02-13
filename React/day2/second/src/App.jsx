import React, { useState } from "react";
import "./App.css";
import { Header } from "./components/Header";
import { Product } from "./components/Products";

function App() {
  const [isShown, setIsShown] = useState(false);

  const showHandler = () => {
    setIsShown(true);
  };

  const hideHandler = () => {
    setIsShown(false);
  };

  return (
    <div className="container text-center">
      {!isShown && (
        <button onClick={showHandler} className="btn btn-primary mb-3">
          Show Products
        </button>
      )}

      {isShown && <Header onHide={hideHandler} />}

      {isShown && <Product />}
    </div>
  );
}

export default App;
