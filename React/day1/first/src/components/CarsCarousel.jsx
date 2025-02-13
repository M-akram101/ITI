import Carousel from "react-bootstrap/Carousel";

function CarsCarousel() {
  return (
    <div className="carousel-container">
      <Carousel data-bs-theme="dark">
        <Carousel.Item>
          <img
            className="d-block w-100"
            src="images/lamborghiny.jpg"
            alt="First Car"
          />
          <Carousel.Caption>
            <h5>Lamborghiny Urus</h5>
            <p>Blue Lambo, new rims with a catchy identity line.</p>
          </Carousel.Caption>
        </Carousel.Item>

        <Carousel.Item>
          <img
            className="d-block w-100"
            src="images/alpharomeo.jpg"
            alt="Second Car"
          />
          <Carousel.Caption>
            <h5>Alpharomeo Giulia</h5>
            <p>
              {" "}
              A car for your everyday use, can park anywhere can go anywhere.
            </p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img className="d-block w-100" src="images/bmw.jpg" alt="Third Car" />
          <Carousel.Caption>
            <h5>BMW 340</h5>
            <p>
              A car for your everyday use, can park anywhere can go anywhere.
            </p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img
            className="d-block w-100"
            src="images/volvo.jpg"
            alt="Fourth Car"
          />
          <Carousel.Caption>
            <h5 className="fs-color-white">Volvo XC40</h5>
            <p>
              A car for your everyday use, can park anywhere can go anywhere.
            </p>
          </Carousel.Caption>
        </Carousel.Item>
      </Carousel>
    </div>
  );
}

export default CarsCarousel;
