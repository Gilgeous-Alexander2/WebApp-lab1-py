// src/components/ScheduleTable.js
import React from 'react';
import './ScheduleTable.css';

const ScheduleTable = () => (
  <div className="schedule-container">
    <table className="schedule-table">
      <thead>
        <tr>
          <th>Петров А.М.</th>
          <th>Предмет 1</th>
          <th>Консультация</th>
          <th>Приём</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Попкова А.А.</td>
          <td className="inactive">Предмет 2</td>
          <td>32.13.3333</td>
          <td>32.13.3333</td>
        </tr>
        <tr>
          <td>Беляев И.С.</td>
          <td className="inactive">Предмет 3</td>
          <td>32.13.3333</td>
          <td>32.13.3333</td>
        </tr>
        {/* Add more rows as necessary */}
      </tbody>
    </table>
    <button className="register-button">записаться</button>
  </div>
);

export default ScheduleTable;
