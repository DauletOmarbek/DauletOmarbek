import { Injectable, OnInit } from '@angular/core';
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";
import {Company} from "./models";

@Injectable({
  providedIn: 'root'
})
export class CompanyService implements OnInit {

  BASE_URL = 'http://127.0.0.1:8000'

  constructor(private client: HttpClient) { }

  getCompanies(): Observable<Company[]>{
    return this.client.get<Company[]>(`${this.BASE_URL}/companies`);
  }

  ngOnInit() {
  }
}
