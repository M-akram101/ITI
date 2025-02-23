import React from "react";
import { Container, Row, Col, Card, Button } from "react-bootstrap";

const listProducts = [
  {
    id: 1,
    name: "Gradient Graphic T-shirt",
    img: "img1",
    rating: 3.5,
    price: 145,
  },
  {
    id: 2,
    name: "Polo with Tipping Details",
    img: "img2",
    rating: 4.5,
    price: 180,
  },
  {
    id: 3,
    name: "Black Striped T-shirt",
    img: "img3",
    rating: 5.0,
    price: 120,
    oldPrice: 150,
    discount: "30%",
  },
  {
    id: 4,
    name: "Skinny Fit Jeans",
    img: "img4",
    rating: 3.5,
    price: 240,
    oldPrice: 260,
    discount: "20%",
  },
  { id: 5, name: "Checkered Shirt", img: "img5", rating: 4.5, price: 180 },
  {
    id: 6,
    name: "Sleeve Striped T-shirt",
    img: "img6",
    rating: 4.5,
    price: 130,
    oldPrice: 160,
    discount: "30%",
  },
  {
    id: 7,
    name: "Vertical Striped Shirt",
    img: "img7",
    rating: 5.0,
    price: 212,
    oldPrice: 232,
    discount: "20%",
  },
  {
    id: 8,
    name: "Courage Graphic T-shirt",
    img: "img8",
    rating: 4.0,
    price: 145,
  },
  {
    id: 9,
    name: "Loose Fit Bermuda Shorts",
    img: "img9",
    rating: 3.0,
    price: 80,
  },
];

export function ProductGrid() {
  return (
    <Container className="mt-4 ms-5">
      {" "}
      {/* Bootstrap classes for spacing */}
      <h2 className="mb-4">Casual</h2>
      <Row>
        {listProducts.map((product) => (
          <Col
            key={product.id}
            md={4}
            className="mb-4 d-flex justify-content-center"
          >
            <Card className="shadow-sm" style={{ width: "18rem" }}>
              <Card.Img
                variant="top"
                src={`/productImage/${product.img}.jpg`}
                alt={product.name}
                className="img-fluid"
              />
              <Card.Body>
                <Card.Title>{product.name}</Card.Title>
                <Card.Text>
                  ⭐ {product.rating}/5
                  <br />
                  {product.oldPrice ? (
                    <>
                      <span className="text-muted text-decoration-line-through">
                        ${product.oldPrice}
                      </span>{" "}
                      <span className="text-danger">-{product.discount}</span>
                    </>
                  ) : null}
                  <br />
                  <strong>${product.price}</strong>
                </Card.Text>
                <Button variant="primary" className="w-100">
                  View
                </Button>
              </Card.Body>
            </Card>
          </Col>
        ))}
      </Row>
    </Container>
  );
}
