import { useEffect, useState } from 'react';
import SearchIcon from '@mui/icons-material/Search';

import { fetchSkills } from '../../../http/skills';
import type { SkillType } from '../../../types/jobs';

import Input from '../../components/Input/Input';
import Loading from '../../components/Loading/Loading';
import SearchSelect from '../../components/SearchSelect/SearchSelect';

import styles from "./filters.module.css";

const Filters = () => {

  const [skills, setSkills] = useState<SkillType[]>([]);
  const [selectedSkills, setSelectedSkills] = useState<SkillType[]>([]);

  const addSelectedSkills = (skill: SkillType) => {
    setSelectedSkills([...selectedSkills, skill])
  }

  const deleteSelectedSkill = (skill: SkillType) => {
    const index = selectedSkills.indexOf(skill);
    if (index != -1){
      setSelectedSkills(selectedSkills.toSpliced(index, 1))
    }
  }

  useEffect(() => {
    fetchSkills().then(data => {
      setSkills(data);
    });
  }, [])

  return (
    <div className={styles.filters}>
      <h2>Search and filtration</h2>
      <div className={styles.filter_options}>
        <div className={styles.filters_input}>
          <span className={styles.filter_input_title}>Salary from</span>
          <Input
            className={styles.salary_input}
            placeholder='Salary'
            type='number'
          />
        </div>
        <div className={styles.filters_input}>
          <span className={styles.filter_input_title}>Salary to</span>
          <Input
            className={styles.salary_input}
            placeholder='Salary'
            type='number'
          />
        </div>
        <div className={styles.filters_input}>
          <span className={styles.filter_input_title}>Experience</span>
          <Input
            className={`${styles.salary_input} ${styles.experience_input}`}
            placeholder='min'
            type='number'
          />
        </div>
        <div className={styles.filters_input}>
          <span className={styles.filter_input_title}>Education</span>
          <select className={styles.filters_select} name="" id="">
            <option value="">None</option>
            <option value="">Bachelor</option>
            <option value="">Master</option>
            <option value="">Doctorate</option>
          </select>
        </div>
      </div>
      <div className={styles.filter_options}>
        <Input isSearch={true} placeholder='Search...' />
        {skills.length > 0 ?
          <>
            <SearchSelect
              skills={skills.filter((skill) => !selectedSkills.includes(skill))}
              addSelectedSkills={addSelectedSkills}
            />
            <SearchSelect
              skills={skills.filter((skill) => !selectedSkills.includes(skill))}
              addSelectedSkills={addSelectedSkills}
            />
          </>  
          : <Loading />
      }
      </div>
      <div className={styles.selected_skills}>
        {selectedSkills.map((skill: SkillType) =>
          <span
            className={styles.selected_skill}
            key={`sel${skill.id}`}
            onClick={() => deleteSelectedSkill(skill)}
          >
            {skill.name}
          </span>
        )}
      </div>
      <div className={styles.filters_footer}>
        <div className={styles.search_button}>
          <span className={styles.search_icon}>
            <SearchIcon fontSize='small' />
          </span>
          Search
        </div>
      </div>
    </div>
  );
}

export default Filters;