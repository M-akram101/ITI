// import { StrictMode } from 'react'
import { createRoot } from "react-dom/client"; // has direct access on dom
import "bootstrap/dist/css/bootstrap.min.css";
import "./index.css";
import App from "./App.jsx"; // app component

createRoot(document.getElementById("root")).render(<App />); //rendering app component el gwaha kol haga htkoon andena || hena hwa hatt app component gwa root

//component = class or function
