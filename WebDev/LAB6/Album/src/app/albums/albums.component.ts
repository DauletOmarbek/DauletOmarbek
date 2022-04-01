import { Component, OnInit } from '@angular/core';
import { Album } from '../models';
import {AlbumsService} from "../albums.service";

@Component({
  selector: 'app-albums',
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css']
})
export class AlbumsComponent implements OnInit {
  albums!: Album[];
  loaded!: boolean;
  newAlbum: string;
  idd!: number;
  boolsearch!: boolean;
  searchtext!: string;
 
  constructor(private albumsService: AlbumsService) { 
    this.newAlbum = '';
  }

  ngOnInit(): void {
    this.getAlbums();
    this.idd = 100;
    this.boolsearch = false;
    this.searchtext = "";

  }

  getAlbums(){
    this.loaded = false;
    this.albumsService.getAlbums().subscribe((albums) =>{
      this.albums = albums;
      this.loaded = true;
    });
  }

  addAlbum(){
    this.idd = this.idd + 1;
    const album = {
      id: this.idd,
      title: this.newAlbum
      
    };
    this.loaded = false;
    this.albumsService.addAlbum(album as Album).subscribe((album) => { 
    });
    this.albums.unshift(album);
    this.newAlbum='';
    this.loaded = true;

  }
  deleteAlbum(id:number){
    this.albums = this.albums.filter((x) => x.id !==id);
    this.albumsService.deleteAlbum(id).subscribe(() =>{
      console.log('delete', id);
    });
  }

  bsearch(text: string){
    if(text == ""){
      this.boolsearch = false;
    }
    else{
      this.boolsearch = true
    }
  }

  search(x: string, y:string){
    var i:number;
    var s:string;
    s = "";
    for(i = 0; i < y.length; i++){
      s = s + x[i];
    }
    if(s == y){
      return true;
    }
    else{
      return false;
    }
  }

}
