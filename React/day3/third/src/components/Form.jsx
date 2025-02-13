import Form from "react-bootstrap/Form";
import { useState } from "react";

function CarRequestForm({ carList, setCarList }) {
  let [form, setForm] = useState({
    name: "",
    carBrand: "",
    carModel: "",
    email: "",
    isAvailable: true,
  });

  let inputHandler = (e) => {
    setForm({
      ...form,
      [e.target.name]:
        e.target.name == "isAvailable" ? e.target.checked : e.target.value,
    });
  };
  const addCarReuest = (e) => {
    e.preventDefault();
    setCarList([...carList, form]);
    setForm({
      name: "",
      carBrand: "",
      carModel: "",
      isAvailable: true,
    });
  };

  const deleteLastCarRequest = () => {
    if (carList.length > 0) {
      setCarList(carList.slice(0, -1));
    }
  };

  return (
    <Form
      onSubmit={addCarReuest}
      class="p-4 border rounded shadow-lg bg-secondary"
    >
      <Form.Group className="m-3" controlId="formGroupName">
        <Form.Label>
          {" "}
          <strong>Name </strong>
        </Form.Label>
        <Form.Control
          value={form.name}
          type="text"
          placeholder="Enter name"
          name="name"
          onChange={inputHandler}
        />
      </Form.Group>
      <Form.Group className="m-3" controlId="formGroupModel">
        <Form.Label>
          {" "}
          <strong>Car Brand</strong>
        </Form.Label>
        <Form.Control
          value={form.carBrand}
          type="text"
          placeholder="Enter Car Brand"
          name="carBrand"
          onChange={inputHandler}
        />
      </Form.Group>
      <Form.Group className="m-3" controlId="formGroupBrand">
        <Form.Label>
          <strong>Car Model</strong>
        </Form.Label>
        <Form.Control
          value={form.carModel}
          type="text"
          placeholder="Enter Car Model"
          name="carModel"
          onChange={inputHandler}
        />
      </Form.Group>
      <Form.Group className="m-3 " controlId="formGroupEmail">
        <Form.Label>
          <strong>Email Address</strong>
        </Form.Label>
        <Form.Control
          onChange={inputHandler}
          value={form.email}
          type="text"
          name="email"
          placeholder="Enter your email"
        />
      </Form.Group>

      <Form.Group className="m-3" controlId="formGroupCheck">
        {" "}
        <strong>Is this Car Available ?</strong>
        <Form.Check
          value={form.isAvailable}
          onChange={inputHandler}
          name="isAvailable"
          checked={form.isAvailable}
          type="checkbox"
        ></Form.Check>
      </Form.Group>
      <div class="d-flex justify-content-center">
        <button className="btn btn-success m-3 my-5 p-3" type="submit">
          {" "}
          Add New Request
        </button>

        <button
          className="btn btn-danger m-3 my-5 p-3"
          type="button"
          onClick={deleteLastCarRequest}
        >
          Delete
        </button>
      </div>
    </Form>
  );
}

export default CarRequestForm;
