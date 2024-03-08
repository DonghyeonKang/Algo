import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        ArrayList<Piece> arr = new ArrayList<Piece>();
        for(int i = 0; i < n; i++) {
            Piece p = new Piece(i + 1);
            arr.add(p);
        }

        int pointer = 0;
        int cnt = 1;
        String str = "<";

        while(arr.size() > 0) {
            System.out.print("pointer : ");
            System.out.println(pointer);
            if(cnt == 3) {
                Piece rp = arr.remove(pointer);
                System.out.println(rp.num.toString() + "추가");
                str += rp.num.toString() + ", ";
                cnt = 1;
            } else {
                cnt += 1;
            }

            pointer += 1;
            if(pointer > (arr.size() - 1)) {
                pointer -= (arr.size() - 1);
            }
        }

        str.substring(0, str.length() - 2);
        System.out.println(str + ">");
    }

    static class Piece {
        public Integer num;

        public Piece(int num) {
            this.num = num;
        }
    }
}