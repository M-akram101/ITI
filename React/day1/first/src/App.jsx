import "./App.css";
import Header from "./components/Header";
import "bootstrap/dist/css/bootstrap.min.css";
import CarsCarousel from "./components/CarsCarousel";
import Footer from "./components/footer";

function App() {
  return (
    <>
      <Header></Header>
      <CarsCarousel></CarsCarousel>
      <Footer></Footer>
    </>
  );
}

export default App;
