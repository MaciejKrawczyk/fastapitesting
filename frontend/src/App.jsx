import {useEffect, useState} from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from "axios";


const api = axios.create({
    baseURL: 'http://localhost:8000/'
})

function App() {
    const [count, setCount] = useState(0)
    const [students, setStudents] = useState([])

    useEffect(() => {
        api.get('/get-students').then(res => {
            setStudents(res.data.data)
        })
        }, [])


  return (
    <div className="App">
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://reactjs.org" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
        </p>
      </div>
      <p className="read-the-docs">
          {students.map(student => <div>{student.first_name} {student.last_name}</div>)}
      </p>
    </div>
  )
}

export default App
