import { render } from "react-dom";
import {BrowserRouter, Routes, Route} from "react-router-dom"
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import App from './App';
import AppWs from './AppWs';
import AppWsA from './AppWsA';

const rootElement = document.getElementById("root");
render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />} />
      <Route path="/ws/:roomId" element={<AppWs />} />
      <Route path="/wsa/" element={<AppWsA />} />
    </Routes>
  </BrowserRouter>,
  rootElement
);