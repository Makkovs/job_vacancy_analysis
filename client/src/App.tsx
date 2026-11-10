import { useEffect } from "react";
import Jobs from "./pages/Jobs/Jobs";
import { fetchJobs } from "./http/jobs";

function App() {

  useEffect(() => {
    fetchJobs().then((data) => {
      console.log(data)
    }
    )
  }, [])

  return (
    <>
      <Jobs />
    </>
  );
}

export default App;
