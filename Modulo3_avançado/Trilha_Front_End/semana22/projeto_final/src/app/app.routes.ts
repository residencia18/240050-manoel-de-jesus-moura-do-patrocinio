import { Routes } from '@angular/router';
import { RegisterAtendComponent } from './pages/register-atend/register-atend.component';
import { ListAtendComponent } from './pages/list-atend/list-atend.component';
import { EditAtendComponent } from './pages/edit-atend/edit-atend.component';
import { RegisterProductComponent } from './pages/register-product/register-product.component';
import { LoginComponent } from './pages/login/login.component';
import { RegisterComponent } from './pages/register/register.component';
import {HomeComponent} from './pages/home/home.component'
import {ProductDetailComponent} from './pages/product-detail/product-detail.component'
import { PainelGerenciaComponent } from './pages/painel-gerencia/painel-gerencia.component';
import { EditProductComponent } from './pages/edit-product/edit-product.component';

export const routes: Routes = [
  {path:"", component: HomeComponent},
  {path:"resgister-atend", component: RegisterAtendComponent},
  {path:"list-atend", component: ListAtendComponent},
  {path:"edit-atend/:id", component: EditAtendComponent},
  {path:"register", component: RegisterComponent},
  {path:"login", component: LoginComponent},
  {path:"painel", component: PainelGerenciaComponent},
  {path:"product/:id", component: ProductDetailComponent},
  {path:"edit-product/:id", component: EditProductComponent},
  {path:"register-product", component: RegisterProductComponent },
];
