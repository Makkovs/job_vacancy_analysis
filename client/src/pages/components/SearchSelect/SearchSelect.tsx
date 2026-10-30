import { useState } from "react";
import { ClickAwayListener } from "@mui/material";

import styles from "./search-select.module.css";

const SearchSelect = () => {
  const skills: string[] = ["Python", "JavaScript", "React", "FastAPI"]

  const [selectHidden, setSelectHidden] = useState<boolean>(true);
  const [skillsToDisplay, setSkillsToDisplay] = useState<string[]>([...skills]);
  const [value, setValue] = useState<string>("");

  const closeSelect = () => {
    setSelectHidden(true);
  }

  const filterSkills = (query: string) => {
    setValue(query)

    const filtered = skills.filter(
      skill => skill.toLocaleLowerCase()
        .includes(query.toLocaleLowerCase())
    )
    setSkillsToDisplay(filtered)
  }

  return (
    <ClickAwayListener onClickAway={closeSelect}>
      <div className={styles.search_select}>
        <input
          type="text"
          placeholder="Select skills"
          value={value}
          onChange={(e) => filterSkills(e.target.value)}
          onClick={() => setSelectHidden(false)}
        />
        <ul
          className={selectHidden ? styles.hidden : styles.select_list}
        >
          {skillsToDisplay.map((skill: string) =>
            <li className={styles.select_item} key={skill}>
              {skill}
            </li>
          )}
        </ul>
      </div>
    </ClickAwayListener>
  );
}

export default SearchSelect;