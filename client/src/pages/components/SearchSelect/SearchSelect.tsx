import { useState } from "react";
import { ClickAwayListener } from "@mui/material";

import type { SkillType } from "../../../types/jobs";

import styles from "./search-select.module.css";

interface SearchSelectProps {
  skills: SkillType[];
  addSelectedSkills: (skill: SkillType) => void;
}

const SearchSelect = ({ skills, addSelectedSkills }: SearchSelectProps) => {
  const [selectHidden, setSelectHidden] = useState<boolean>(true);
  const [value, setValue] = useState<string>("");

  const closeSelect = () => {
    setSelectHidden(true);
  }

  const skillsToDisplay = skills.filter(skill =>
    skill.name.toLocaleLowerCase().includes(value.toLocaleLowerCase())
  );

  return (
    <ClickAwayListener onClickAway={closeSelect}>
      <div className={styles.search_select}>
        <input
          type="text"
          placeholder="Select skills"
          value={value}
          onChange={(e) => setValue(e.target.value)}
          onClick={() => setSelectHidden(false)}
        />
        <ul
          className={selectHidden ? styles.hidden : styles.select_list}
        >
          {skillsToDisplay.map((skill: SkillType) =>
            <li
              className={styles.select_item}
              key={skill.id}
              onClick={() => addSelectedSkills(skill)}
            >
              {skill.name}
            </li>
          )}
        </ul>
      </div>
    </ClickAwayListener>
  );
}

export default SearchSelect;