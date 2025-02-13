import { Badge, Table } from "react-bootstrap";

function CarTable({ carList }) {
  return (
    carList.length > 0 && (
      <Table striped="columns" className="m-3 my-5">
        <thead>
          <tr>
            <th>#</th>
            <th>Name</th>
            <th>Brand</th>
            <th>Model</th>
            <th>email</th>
          </tr>
        </thead>
        <tbody>
          {carList.map((car, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{car.name}</td>
              <td>{car.carBrand}</td>
              <td>{car.carModel}</td>
              <td>
                {car.isAvailable ? (
                  <Badge bg="success">Available</Badge>
                ) : (
                  <Badge bg="danger">Not Available</Badge>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
    )
  );
}

export default CarTable;
