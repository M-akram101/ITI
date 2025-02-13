import Container from "react-bootstrap/Container";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";

function Footer() {
  return (
    <Navbar bg="dark" data-bs-theme="dark" className="mt-auto py-3">
      <Container className="d-flex justify-content-between">
        <span className="text-light">
          &copy; {new Date().getFullYear()} Exotica. All Rights Reserved.
        </span>
        <Nav>
          <Nav.Link href="#privacy" className="text-light">
            Privacy Policy
          </Nav.Link>
          <Nav.Link href="#terms" className="text-light">
            Terms of Use
          </Nav.Link>
        </Nav>
      </Container>
    </Navbar>
  );
}

export default Footer;
