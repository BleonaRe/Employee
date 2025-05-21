// src/components/DashboardCards.js
import React from 'react';

const DashboardCards = ({ totalEmployees, totalAttendance, ongoingProjects }) => (
  <div className="row">
    <div className="col-md-4">
      <div className="card p-3" style={{ backgroundColor: 'gray', color: 'black', borderRadius: '10px', boxShadow: '0px 4px 8px rgba(0,0,0,0.1)' }}>
        <h5>Employees</h5>
        <p>Total: {totalEmployees}</p>
      </div>
    </div>
    <div className="col-md-4">
      <div className="card p-3" style={{ backgroundColor: 'gray', color: 'black', borderRadius: '10px', boxShadow: '0px 4px 8px rgba(0,0,0,0.1)' }}>
        <h5>Attendance</h5>
        <p>Checked-in Today: {totalAttendance}</p>
      </div>
    </div>
    <div className="col-md-4">
      <div className="card p-3" style={{ backgroundColor: 'gray', color: 'black', borderRadius: '10px', boxShadow: '0px 4px 8px rgba(0,0,0,0.1)' }}>
        <h5>Projects</h5>
        <p>Ongoing: {ongoingProjects}</p>
      </div>
    </div>
  </div>
);

export default DashboardCards;
