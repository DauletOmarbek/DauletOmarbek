import { Component, OnInit } from '@angular/core';
import { Vacancy } from '../models';
import { VacancyService } from '../vacancy.service';
import { ActivatedRoute, ParamMap, Router } from '@angular/router';
import {Location} from '@angular/common';

@Component({
  selector: 'app-vacancy-list',
  templateUrl: './vacancy-list.component.html',
  styleUrls: ['./vacancy-list.component.css']
})
export class VacancyListComponent implements OnInit {
  vacancies: Vacancy[]=[];
  loaded!: boolean;
  id=0;


  constructor(private route: ActivatedRoute,
              private location: Location,
              private vacanciesService: VacancyService, 
              private router: Router) { 
    
  }

  ngOnInit(): void {
    this.route.paramMap.subscribe((param: ParamMap)=>{
      let i = Number(param.get('id'));
      this.id=i;
    })
    this.getVacancies();
  }


  getVacancies(){
    this.vacanciesService.getVacancies().subscribe((data)=>{
      this.vacancies = data;
    })
  }
}
