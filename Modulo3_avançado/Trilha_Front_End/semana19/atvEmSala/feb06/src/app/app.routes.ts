import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { paisesResolver } from './resolvers/paises.resolver';

export const routes: Routes = [
  {path: "", component: HomeComponent, resolve: {listaPaises:paisesResolver}}
];
