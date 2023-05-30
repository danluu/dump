import { AbstractDataSource } from "./abstractDataSource";
import { Product, Order } from "./entities";
import Axios from "axios";

// const protocol = "http";
// const hostname = "localhost";
// const port = 4600;

const urls = {
    // products: `${protocol}://${hostname}:${port}/products`,
    // orders: `${protocol}://${hostname}:${port}/orders`
    products: "/api/products",
    orders: "/api/orders"    
}

export class RemoteDataSource extends AbstractDataSource {
    loadProducts(): Promise<Product[]> {
        return Axios.get(urls.products).then(response => response.data);
    }

    storeOrder(): Promise<number> {
        return Axios.post(urls.orders, this.order).then(response => response.data.id);
    }
}