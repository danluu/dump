import { sum } from "./calc";

test("check result value", () => {
        expect(sum(1, 2, 3)).toBe(6);
    }
)