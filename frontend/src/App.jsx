import { useState } from 'react'
import FeedbackForm from './FeedbackForm'
import './App.css'
import FeedbackTable from './FeedbackTable'

function App() {

  return (
    <div className="page">

      <div className="container">
        <FeedbackForm />
      </div>
      <br /><br /><br />
      <div className="table">
        <FeedbackTable />
      </div>
    </div>


  )
}

export default App
