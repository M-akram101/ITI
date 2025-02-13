import { useState } from "react";
import "./App.css";
import CarRequestForm from "./components/form";
import CarTable from "./components/Table";

function App() {
  let [carList, setCarList] = useState([]);
  return (
    <>
      <CarRequestForm
        carList={carList}
        setCarList={setCarList}
      ></CarRequestForm>
      <CarTable carList={carList}></CarTable>
    </>
  );
}

export default App;
