import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { Product, products } from '../products';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {
  constructor(private route: ActivatedRoute) { }
  products = products;
  catag_name = '';
  a = false;
  like = 0;
  ngOnInit(): void {
    const routeParams = this.route.snapshot.paramMap;
  const categoryNameFromRoute = String(routeParams.get('categoryName'));

  // Find the product that correspond with the id provided in route.
  this.catag_name = categoryNameFromRoute;
  }

  foo (text: string, bool: boolean) {
    this.a = false;
    if(text == this.catag_name && bool){
      this.a = true;
    }
  return this.a;
  }

  lik (n: boolean, like: number){
    if (!n){
      return like+1;}
    else{
      return like;
    }
  }
}