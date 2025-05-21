// src/components/Sidebar.js
import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {
  faHome,
  faUsers,
  faCalendarCheck,
  faCalendarAlt,
  faChartLine,
  faTasks,
  faBullseye,
  faBeer,
  faPoll
} from '@fortawesome/free-solid-svg-icons';

const Sidebar = () => {
  return (
    <div
      className="sidebar"
      style={{
        width: '280px',
        height: '100vh',
        background: 'rgba(73, 5, 5, 0.875)',
        color: 'white',
        position: 'fixed',
        padding: '25px',
        top: 0,
        boxShadow: '2px 0px 15px rgba(0, 0, 0, 0.2)',
        overflowY: 'auto',
      }}
    >
      <h4 className="mb-4">📊 Dashboard</h4>
      <a href="/" style={linkStyle}>
        <FontAwesomeIcon icon={faHome} /> Home
      </a>
      <a href="/api/employees/" style={linkStyle}>
        <FontAwesomeIcon icon={faUsers} /> Employees
      </a>
      <a href="/api/attendance/" style={linkStyle}>
        <FontAwesomeIcon icon={faCalendarCheck} /> Attendance
      </a>
      <a href="/api/schedules/" style={linkStyle}>
        <FontAwesomeIcon icon={faCalendarAlt} /> Schedules
      </a>
      <a href="/api/performance-reports/" style={linkStyle}>
        <FontAwesomeIcon icon={faChartLine} /> Performance-reports
      </a>
      <a href="/api/projects/" style={linkStyle}>
        <FontAwesomeIcon icon={faTasks} /> Projects
      </a>
      <a href="/api/goals/" style={linkStyle}>
        <FontAwesomeIcon icon={faBullseye} /> Goals
      </a>
      <a href="/api/holidays/" style={linkStyle}>
        <FontAwesomeIcon icon={faBeer} /> Holidays
      </a>
      <a href="/api/surveys/" style={linkStyle}>
        <FontAwesomeIcon icon={faPoll} /> Surveys
      </a>
    </div>
  );
};

const linkStyle = {
  color: 'white',
  textDecoration: 'none',
  display: 'block',
  padding: '12px',
  marginBottom: '10px',
  borderRadius: '6px',
  fontSize: '18px',
};

export default Sidebar;
