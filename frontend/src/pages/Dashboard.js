// src/pages/Dashboard.js
import React, { useEffect, useRef } from 'react';
import Chart from 'chart.js/auto';

const Dashboard = ({ totalEmployees = 0, totalAttendance = 0, ongoingProjects = 0 }) => {
  const chartRef = useRef(null);
  let chartInstance = useRef(null);

  useEffect(() => {
    if (chartInstance.current) {
      chartInstance.current.destroy();
    }

    const ctx = chartRef.current.getContext('2d');

    chartInstance.current = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Employees', 'Attendance', 'Projects'],
        datasets: [
          {
            label: '# of Items',
            data: [totalEmployees, totalAttendance, ongoingProjects],
            backgroundColor: ['#1ABC9C', '#F39C12', '#3498DB'],
            borderColor: ['#1ABC9C', '#F39C12', '#3498DB'],
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          y: { beginAtZero: true },
        },
        responsive: true,
        maintainAspectRatio: false,
      },
    });

    return () => {
      if (chartInstance.current) {
        chartInstance.current.destroy();
      }
    };
  }, [totalEmployees, totalAttendance, ongoingProjects]);

  return (
    <div className="container mt-4">
      <h2 className="mb-4 text-center">Employee Management Dashboard</h2>
      <div className="d-flex justify-content-center mb-4 gap-4 flex-wrap">
        <div
          className="card p-3"
          style={{
            width: '250px',
            borderRadius: '10px',
            boxShadow: '0px 4px 8px rgba(0, 0, 0, 0.1)',
            backgroundColor: '#cccccc',
            color: 'black',
            textAlign: 'center',
          }}
        >
          <h5>Employees</h5>
          <p>Total: {totalEmployees}</p>
        </div>
        <div
          className="card p-3"
          style={{
            width: '250px',
            borderRadius: '10px',
            boxShadow: '0px 4px 8px rgba(0, 0, 0, 0.1)',
            backgroundColor: '#cccccc',
            color: 'black',
            textAlign: 'center',
          }}
        >
          <h5>Attendance</h5>
          <p>Checked-in Today: {totalAttendance}</p>
        </div>
        <div
          className="card p-3"
          style={{
            width: '250px',
            borderRadius: '10px',
            boxShadow: '0px 4px 8px rgba(0, 0, 0, 0.1)',
            backgroundColor: '#cccccc',
            color: 'black',
            textAlign: 'center',
          }}
        >
          <h5>Projects</h5>
          <p>Ongoing: {ongoingProjects}</p>
        </div>
      </div>

      <div style={{ height: '350px', maxWidth: '700px', margin: '0 auto' }}>
        <h4 className="mb-4 text-center">Employee Overview</h4>
        <canvas id="employeeChart" ref={chartRef}></canvas>
      </div>
    </div>
  );
};

export default Dashboard;
