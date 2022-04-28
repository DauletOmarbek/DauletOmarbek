import { Component, OnInit } from '@angular/core';
import { Company } from '../models';
import { CompanyService } from '../company.service';

@Component({
  selector: 'app-company-list',
  templateUrl: './company-list.component.html',
  styleUrls: ['./company-list.component.css']
})
export class CompanyListComponent implements OnInit {
  companies!: Company[];
  loaded!: boolean;


  constructor(private companiesService: CompanyService) { 
    
  }

  ngOnInit(): void {
    this.getCompanies()
  }


  getCompanies(){
    this.loaded = false;
    this.companiesService.getCompanies().subscribe((companies) =>{
      this.companies = companies;
      this.loaded = true;
    });
  }
}
