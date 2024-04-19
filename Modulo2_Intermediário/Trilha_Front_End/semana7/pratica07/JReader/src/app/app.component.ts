import { Component } from '@angular/core';
import { CommonModule, NgIf } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { ClasseComponent } from './components/classe/classe.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { type_veiculos, veiculosObj } from '../types/types';
import { ObjetoComponent } from './components/objeto/objeto.component';
import { PropriedadeComponent } from './components/propriedade/propriedade.component';
import { ValorPropriedadeComponent } from './components/valor-propriedade/valor-propriedade.component';
import { FooterComponent } from './components/footer/footer.component';
import { ApiService } from './services/api-service.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, NgIf, RouterOutlet, HttpClientModule,
    ClasseComponent, ObjetoComponent,
    PropriedadeComponent, ValorPropriedadeComponent,
    FooterComponent
  ],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService]
})
export class AppComponent {

  result: any;
  urlToJson = '../assets/veiculos.json';
  categorySelect: veiculosObj
  veiculoSelect: (type_veiculos | null);
  propSelect: string;
  veiculoList: type_veiculos[] = [];

  constructor(public http: HttpClient) {
    this.categorySelect = {categoria:"",items:[]}
    this.veiculoSelect = null
    this.propSelect = ""
  }

  // constructor(private veiculoServico: ApiService) {
  //   this.categorySelect = { categoria: "", items: [] }
  //   this.veiculoSelect = null
  //   this.propSelect = ""
  // }
  ngOnInit(): void {
    this.http.get<any>(this.urlToJson).subscribe(response => {
      this.result = response;
    });
  }

  // ngOnInit(): void {
  //   this.veiculoServico.getVeiculos().subscribe((response) => {
  //     const name = response.map((item:any)=>{
  //       return item.name
  //     })
  //     console.log("veiculoServico",response)
  //     this.result = name;
  //   })
  // }
  setCategorySelected(event: veiculosObj) {
    this.categorySelect = event;
  }
  setVeiculoSelected(veiculo: type_veiculos) {
    this.veiculoSelect = veiculo;
  }
  setPropSelected(prop: string) {
    this.propSelect = prop;
  }

  addVeiculos(veiculo: type_veiculos) {
    veiculo && !this.veiculoList.includes(veiculo) && this.veiculoList.push(veiculo);
  }
  title = 'JReader';
}
